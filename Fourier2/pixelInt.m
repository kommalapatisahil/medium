%to visualizze the magnitude of the pup image

F = imread('pippt.png');
B = transpose(rgb2gray(F));

figure();
surf(uint8(B(20:20:end, 20:20:end)));
title('Pixel Intensities- Bed sheet view'); 
colormap(parula(20));
%this colormap shows the most clear results
%play with 20 to see how it affects the gif.