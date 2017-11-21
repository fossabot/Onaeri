briRange         = (1, 254)     # [min, max] brightness in val, unsigned int
colorRange       = (2200, 4000) # [min, max] color temp in val, unsigned int

brightnessData = { "day": 100, "night": 0, "morning": (0,0,0,0,0,0,0,0,0,0.2,0.4,0.7,0.9,1.3,1.8,2.4,3,3.6,4.2,5,5.8,6.5,7.1,7.7,8.5,9.3,10,10.6,11.2,12,12.8,13.5,14,14.6,15.4,16.2,16.9,17.4,18.1,18.8,19.7,20.4,20.9,21.5,22.3,23.1,23.8,24.5,25.3,26.2,27.1,27.8,28.4,29.2,30,30.7,31.3,31.9,32.7,33.5,34.2,34.7,35.4,36.2,37,37.7,38.2,38.9,39.6,40.4,41.1,41.7,42.3,43,43.9,44.5,45.1,45.7,46.5,47.3,48,48.7,49.5,50.4,51.3,52,52.7,53.5,54.3,55,55.5,56.1,56.9,57.7,58.3,58.9,59.5,60.2,61,61.7,62.2,62.8,63.5,64.3,64.9,65.4,65.9,66.6,67.4,68,68.5,69,69.7,70.4,71,71.5,72.1,72.9,73.5,74.1,74.6,75.2,75.8,76.3,76.7,77.2,77.7,78.3,78.7,79.1,79.5,80,80.5,81,81.3,81.7,82.1,82.6,83,83.3,83.7,84.1,84.5,84.9,85.2,85.5,85.8,86.2,86.5,86.9,87.2,87.6,88,88.3,88.6,88.9,89.2,89.5,89.7,90,90.2,90.5,90.7,90.9,91.1,91.4,91.6,91.8,92,92.2,92.4,92.7,92.9,93,93.2,93.4,93.6,93.7,93.8,94,94.2,94.3,94.5,94.6,94.8,94.9,95.1,95.2,95.3,95.5,95.6,95.7,95.8,95.9,96.1,96.2,96.3,96.4,96.5,96.6,96.7,96.8,96.8,96.9,97,97.1,97.2,97.2,97.3,97.4,97.5,97.5,97.6,97.6,97.7,97.8,97.8,97.9,97.9,98,98.1,98.2,98.2,98.3,98.3,98.4,98.4,98.5,98.5,98.5,98.6,98.6,98.7,98.7,98.7,98.8,98.8,98.8,98.9,98.9,98.9,99,99,99,99,99,99.1,99.1,99.1,99.1,99.2,99.2,99.2,99.2,99.2,99.3,99.3,99.3,99.3,99.3,99.4,99.4,99.4,99.4,99.4,99.5,99.5,99.5,99.5,99.5,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100), \
"evening": (100,100,100,100,100,99.9,99.9,99.9,99.9,99.9,99.8,99.8,99.8,99.8,99.7,99.7,99.7,99.6,99.6,99.6,99.5,99.5,99.5,99.4,99.4,99.3,99.3,99.3,99.2,99.2,99.1,99.1,99,99,98.9,98.9,98.8,98.7,98.7,98.6,98.6,98.5,98.5,98.4,98.3,98.3,98.2,98.1,98.1,98,97.9,97.9,97.8,97.7,97.7,97.6,97.5,97.4,97.4,97.3,97.2,97.1,97,97,96.9,96.8,96.7,96.6,96.6,96.5,96.4,96.3,96.2,96.1,96,95.9,95.8,95.8,95.7,95.6,95.5,95.4,95.3,95.2,95.1,95,94.9,94.8,94.7,94.6,94.5,94.4,94.3,94.2,94.1,94,93.8,93.7,93.6,93.5,93.4,93.3,93.2,93.1,93,92.8,92.7,92.6,92.5,92.4,92.3,92.1,92,91.9,91.8,91.7,91.5,91.4,91.3,91.2,91,90.9,90.8,90.7,90.5,90.4,90.3,90.1,90,89.9,89.7,89.6,89.5,89.3,89.2,89.1,88.9,88.8,88.7,88.5,88.4,88.2,88.1,88,87.8,87.7,87.5,87.4,87.2,87.1,86.9,86.8,86.6,86.5,86.3,86.2,86,85.9,85.7,85.6,85.4,85.3,85.1,85,84.8,84.7,84.5,84.3,84.2,84,83.9,83.7,83.5,83.4,83.2,83.1,82.9,82.7,82.6,82.4,82.2,82.1,81.9,81.7,81.6,81.4,81.2,81,80.9,80.7,80.5,80.3,80.2,80,79.8,79.6,79.5,79.3,79.1,78.9,78.8,78.6,78.4,78.2,78,77.9,77.7,77.5,77.3,77.1,76.9,76.7,76.6,76.4,76.2,76,75.8,75.6,75.4,75.2,75,74.8,74.7,74.5,74.3,74.1,73.9,73.7,73.5,73.3,73.1,72.9,72.7,72.5,72.3,72.1,71.9,71.7,71.5,71.3,71.1,70.9,70.7,70.5,70.3,70.1,69.8,69.6,69.4,69.2,69,68.8,68.6,68.4,68.2,68,67.7,67.5,67.3,67.1,66.9,66.7,66.5,66.2,66,65.8,65.6,65.4,65.1,64.9,64.7,64.5,64.3,64,63.8,63.6,63.4,63.1,62.9,62.7,62.5,62.2,62,61.8,61.5,61.3,61.1,60.9,60.6,60.4,60.2,59.9,59.7,59.5,59.2,59,58.7,58.5,58.3,58,57.8,57.6,57.3,57.1,56.8,56.6,56.4,56.1,55.9,55.6,55.4,55.1,54.9,54.7,54.4,54.2,53.9,53.7,53.4,53.2,52.9,52.7,52.4,52.2,51.9,51.7,51.4,51.2,50.9,50.7,50.4,50.1,49.9,49.6,49.4,49.1,48.9,48.6,48.3,48.1,47.8,47.6,47.3,47,46.8,46.5,46.3,46,45.7,45.5,45.2,44.9,44.7,44.4,44.1,43.9,43.6,43.3,43.1,42.8,42.5,42.2,42,41.7,41.4,41.2,40.9,40.6,40.3,40.1,39.8,39.5,39.2,39,38.7,38.4,38.1,37.8,37.6,37.3,37,36.7,36.4,36.2,35.9,35.6,35.3,35,34.7,34.5,34.2,33.9,33.6,33.3,33,32.7,32.4,32.1,31.9,31.6,31.3,31,30.7,30.4,30.1,29.8,29.5,29.2,28.9,28.6,28.3,28,27.7,27.4,27.1,26.9,26.6,26.3,26,25.7,25.3,25,24.7,24.4,24.1,23.8,23.5,23.2,22.9,22.6,22.3,22,21.7,21.4,21.1,20.8,20.5,20.2,19.8,19.5,19.2,18.9,18.6,18.3,18,17.7,17.3,17,16.7,16.4,16.1,15.8,15.4,15.1,14.8,14.5,14.2,13.9,13.5,13.2,12.9,12.6,12.3,11.9,11.6,11.3,11,10.6,10.3,10,9.7,9.3,9,8.7,8.4,8,7.7,7.4,7,6.7,6.4,6,5.7,5.4,5,4.7,4.4,4,3.7,3.4,3,2.7,2.4,2,1.7,1.4,1,0.7,0.3,0) }
# Evening: y = -(100 / (500^1.7))x^1.7 + 100 for 1 <= x <= 500

colorData = { "day": 100, "night": 0, "morning": (0,0,0,0,0,0.3,0.6,1,1.3,1.8,2.3,2.9,3.3,3.8,4.3,4.9,5.5,6,6.5,7,7.6,8,8.4,8.8,9.4,9.9,10.4,10.8,11.2,11.8,12.3,12.8,13.2,13.6,14.2,14.7,15.2,15.6,16.2,16.8,17.4,17.9,18.3,18.9,19.4,19.9,20.3,20.7,21.2,21.8,22.2,22.6,23.1,23.6,24.1,24.6,25,25.4,25.9,26.5,27,27.4,28,28.6,29.2,29.7,30.2,30.7,31.3,31.7,32.1,32.5,33.1,33.6,34.1,34.5,34.9,35.4,36,36.5,36.8,37.3,37.8,38.3,38.8,39.3,39.8,40.5,41,41.5,42,42.5,43.1,43.5,43.9,44.4,44.9,45.4,45.9,46.3,46.7,47.2,47.8,48.3,48.6,49.1,49.6,50.2,50.7,51.1,51.7,52.3,52.9,53.4,53.8,54.3,54.9,55.4,55.7,56.1,56.7,57.2,57.7,58,58.5,59,59.5,60,60.3,60.8,61.3,61.8,62.2,62.6,63,63.5,64,64.4,64.8,65.3,65.9,66.4,66.8,67.2,67.7,68.2,68.6,68.9,69.3,69.7,70.2,70.6,70.9,71.3,71.7,72.2,72.5,72.8,73.2,73.6,74,74.4,74.7,75.1,75.6,76,76.4,76.7,77.1,77.5,77.8,78.1,78.3,78.7,79.1,79.4,79.6,79.9,80.2,80.6,80.9,81.1,81.4,81.7,82,82.3,82.6,82.9,83.2,83.5,83.8,84.1,84.3,84.6,84.9,85.1,85.3,85.6,85.8,86.1,86.2,86.4,86.7,86.9,87.2,87.3,87.5,87.8,88,88.2,88.4,88.6,88.8,89,89.2,89.4,89.6,89.8,90,90.1,90.3,90.5,90.7,90.9,91,91.1,91.3,91.5,91.6,91.7,91.9,92,92.2,92.3,92.4,92.6,92.7,92.9,93,93.1,93.2,93.4,93.5,93.6,93.7,93.8,94,94.1,94.2,94.2,94.4,94.5,94.6,94.7,94.7,94.8,95,95,95.1,95.2,95.3,95.4,95.4,95.5,95.6,95.7,95.8,95.9,96,96.1,96.1,96.2,96.3,96.3,96.4,96.5,96.6,96.6,96.7,96.8,96.8,96.9,96.9,97,97,97.1,97.1,97.2,97.2,97.3,97.4,97.4,97.5,97.5,97.6,97.6,97.7,97.7,97.8,97.8,97.9,97.9,97.9,98,98,98,98.1,98.1,98.1,98.2,98.2,98.2,98.3,98.3,98.3,98.4,98.4,98.4,98.5,98.5,98.5,98.6,98.6,98.6,98.6,98.7,98.7,98.7,98.7,98.8,98.8,98.8,98.8,98.8,98.9,98.9,98.9,98.9,98.9,99,99,99,99,99.1,99.1,99.1,99.1,99.1,99.2,99.2,99.2,99.2,99.2,99.3,99.3,99.3,99.3,99.3,99.3,99.3,99.3,99.3,99.4,99.4,99.4,99.4,99.4,99.4,99.4,99.4,99.4,99.4,99.5,99.5,99.5,99.5,99.5,99.5,99.5,99.5,99.5,99.5,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,99.9,100,100,100,100,100,100,100,100), \
"evening": (100,99.9,99.9,99.9,99.9,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.8,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.7,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.6,99.5,99.5,99.5,99.5,99.5,99.5,99.5,99.4,99.4,99.4,99.4,99.4,99.3,99.3,99.3,99.3,99.3,99.2,99.2,99.2,99.2,99.1,99.1,99.1,99.1,99,99,99,98.9,98.9,98.9,98.8,98.8,98.8,98.7,98.7,98.7,98.6,98.6,98.5,98.5,98.4,98.4,98.3,98.2,98.2,98.1,98.1,98,98,97.9,97.8,97.8,97.7,97.6,97.6,97.5,97.4,97.3,97.2,97.2,97.1,97,96.9,96.8,96.7,96.6,96.5,96.4,96.3,96.2,96.1,96,95.8,95.7,95.6,95.5,95.3,95.2,95,94.9,94.8,94.6,94.4,94.3,94.1,93.9,93.8,93.6,93.4,93.2,93,92.8,92.6,92.4,92.2,92,91.7,91.5,91.3,91,90.8,90.5,90.2,90,89.7,89.4,89.1,88.8,88.5,88.2,87.9,87.5,87.2,86.9,86.5,86.1,85.8,85.4,85,84.6,84.2,83.8,83.4,83,82.5,82.1,81.6,81.2,80.7,80.2,79.7,79.3,78.7,78.2,77.7,77.2,76.6,76.1,75.5,75,74.4,73.8,73.2,72.6,72,71.4,70.8,70.1,69.5,68.8,68.2,67.5,66.8,66.2,65.5,64.8,64.1,63.4,62.7,61.9,61.2,60.5,59.8,59,58.3,57.6,56.8,56.1,55.3,54.6,53.8,53,52.3,51.5,50.8,50,49.2,48.5,47.7,47,46.2,45.4,44.7,43.9,43.2,42.4,41.7,41,40.2,39.5,38.8,38.1,37.3,36.6,35.9,35.2,34.5,33.8,33.2,32.5,31.8,31.2,30.5,29.9,29.2,28.6,28,27.4,26.2,25.6,25,24.5,23.9,23.4,22.8,22.3,21.8,21.3,20.7,20.3,19.8,19.3,18.8,18.4,17.9,17.5,17,16.6,16.2,15.8,15.4,15,14.6,14.2,13.9,13.5,13.1,12.8,12.5,12.1,11.8,11.5,11.2,10.9,10.6,10.3,10,9.8,9.5,9.2,9,8.7,8.5,8.3,8,7.8,7.6,7.4,7.2,7,6.8,6.6,6.4,6.2,6.1,5.9,5.7,5.6,5.4,5.2,5.1,5,4.8,4.7,4.5,4.4,4.3,4.2,4,3.9,3.8,3.7,3.6,3.5,3.4,3.3,3.2,3.1,3,2.9,2.8,2.8,2.7,2.6,2.5,2.4,2.4,2.3,2.2,2.2,2.1,2,2,1.9,1.9,1.8,1.8,1.7,1.7,1.6,1.6,1.5,1.5,1.4,1.4,1.3,1.3,1.3,1.2,1.2,1.2,1.1,1.1,1.1,1,1,1,0.9,0.9,0.9,0.9,0.8,0.8,0.8,0.8,0.7,0.7,0.7,0.7,0.7,0.6,0.6,0.6,0.6,0.6,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) }


# y = -0.0001x^3+100 for 0 <= x <= 99
deviationData = (100,100,100,100,100,100,100,100,99.9,99.9,99.9,99.9,99.8,99.8,99.7,99.7,99.6,99.5,99.4,99.3,99.2,99.1,98.9,98.8,98.6,98.4,98.2,98,97.8,97.6,97.3,97,96.7,96.4,96.1,95.7,95.3,94.9,94.5,94.1,93.6,93.1,92.6,92,91.5,90.9,90.3,89.6,88.9,88.2,87.5,86.7,85.9,85.1,84.3,83.4,82.4,81.5,80.5,79.5,78.4,77.3,76.2,75,73.8,72.5,71.3,69.9,68.6,67.1,65.7,64.2,62.7,61.1,59.5,57.8,56.1,54.3,52.5,50.7,48.8,46.9,44.9,42.8,40.7,38.6,36.4,34.1,31.9,29.5,27.1,24.6,22.1,19.6,16.9,14.3,11.5,8.7,5.9,3)
