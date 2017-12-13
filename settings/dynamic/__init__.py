import json
import os
import time
from ...logger import log
from .. import Global

blacklist = ['__init__.py']
expectedExtention = "json"
folderPath = os.path.dirname(os.path.abspath(__file__))
fileTemplate = {
    'min': {'brightness': Global.valRange[0], 'color': Global.valRange[0]},
    'max': {'brightness': Global.valRange[1], 'color': Global.valRange[1]},
    'meta': {'called': 0, 'created': time.time()}
}


def get(id, groups=None):
    filePath = "%s/%s.%s" % (folderPath, id, expectedExtention)
    try:
        content = json.load(open(filePath))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        _reset(id)
        return fileTemplate

    ret = {}
    if groups is not None:
        if type(groups) is str or type(groups) is int:
            # Make groups iterable if it isn't
            groups = [groups]

        for group in groups:
            try:
                ret[group] = content[group]
            except KeyError:
                _reset(id)
    else:
        ret = content

    set(id, 'meta', {'called': time.time()})

    return ret


def set(id, group, data, keys=None):
    filePath = "%s/%s.%s" % (folderPath, id, expectedExtention)
    try:
        content = json.load(open(filePath))
    except FileNotFoundError:
        _reset(id)
        set(id, group, data, keys)
    except json.decoder.JSONDecodeError:
        _reset(id)
        set(id, group, data, keys)

    if type(data) is dict:
        if group not in content:
            content[group] = {}
        if keys is None:
            keys = []
            for key in data:
                keys.append(key)

        for k in keys:
            if data[k] is not None:
                content[group][k] = data[k]
            else:
                log.error("It happened! %s" % k)

        with open(filePath, 'w') as f:
            f.write(json.dumps(content))
    else:
        log.error("[Settings][Dynamic] Unexpected datatype provided")
        log("Data provided:")
        log("type: %s" % type(data))
        log(data)
        exit()


def list():
    files = [f for f in os.listdir(folderPath)
             if os.path.isfile(os.path.join(folderPath, f))
             and not f.startswith(".") and f not in blacklist]

    ret = []
    for f in files:
        if f.endswith(".%s" % expectedExtention):
            ret.append(f.split(".%s" % expectedExtention)[0])
    return ret


def _reset(id):
    log.warn("Dynamic settings for `%s` have been reset." % id)

    filePath = "%s/%s.%s" % (folderPath, id, expectedExtention)
    with open(filePath, 'w') as f:
        f.write(json.dumps(fileTemplate))


def _cleanup(days=Global.dynamicSettingsKeep):
    """
    Remove old dynamic settings
    """
    for f in list():
        f = "%s.%s" % (f, expectedExtention)
        remove = False
        path = os.path.join(folderPath, f)

        try:
            content = json.load(open(path))
        except json.decoder.JSONDecodeError:
            # Can't parse the file as JSON, so lets toss it.
            remove = True
        else:
            if content['meta']['called'] < (time.time() - (days * 86400)):
                if not content['meta']['called'] == 0:
                    remove = True

        if remove:
            os.remove(path)
            log("[Cleanup] Removed old dynamic settings file `%s`." % f)


_cleanup()
