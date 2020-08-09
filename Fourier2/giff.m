%to visualizze the magnitude of the pup image

F = imread('pippt.png');
B = transpose(rgb2gray(F));

figure();
surf(uint8(B(20:20:end, 20:20:end)));
title('Pixel Intensities- Bed sheet view'); 
colormap(parula(20));
%this colormap shows the most clear results
%play with 20 to see how it affects the gif.

rotating_gif = 1;

%reference - 
%https://www.mathworks.com/matlabcentral/answers/86940-animate-3d-plot-view

if rotating_gif

grid on
az = 0;
el = 90;
view([az,el])
degStep = 1;
detlaT = 0.05;
fCount = 71;
%f = getframe(gcf);
[im,map] = rgb2ind(f.cdata,256,'nodither');
im(1,1,1,fCount) = 0;
k = 1;
% spin 45°

for i = 0:-degStep:-45
  az = i;
  ([az,el])
  f = getframe(gcf);
  im(:,:,1,k) = rgb2ind(f.cdata,map,'nodither');
  k = k + 1;
end
% tilt down
for i = 90:-degStep:15
  el = i;
  view([az,el])
  f = getframe(gcf);
  im(:,:,1,k) = rgb2ind(f.cdata,map,'nodither');
  k = k + 1;
end
% spin left
for i = az:-degStep:-90
  az = i;
  view([az,el])
  f = getframe(gcf);
  im(:,:,1,k) = rgb2ind(f.cdata,map,'nodither');
  k = k + 1;
end
% spin right
for i = az:degStep:0
  az = i;
  view([az,el])
  f = getframe(gcf);
  im(:,:,1,k) = rgb2ind(f.cdata,map,'nodither');
  k = k + 1;
end
% tilt up to original
for i = el:degStep:90
  el = i;
  view([az,el])
  f = getframe(gcf);
  im(:,:,1,k) = rgb2ind(f.cdata,map,'nodither');
  k = k + 1; 
end
imwrite(im,map,'Animation.gif','DelayTime',detlaT,'LoopCount',inf)

end
