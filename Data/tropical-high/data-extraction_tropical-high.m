%get WPSH index from ERA-I H850
clear
fname='H850mm.nc';
nci=ncinfo(fname);
 
t=ncread(fname,'time');
lat=ncread(fname,'latitude');
lon=ncread(fname,'longitude');
z=ncread(fname,'z');
% {'hours since 1900-01-01 00:00:0.0'}
t0=datenum(1900,1,1);
WPt=t0+t/24;
% 15°N–25°N, 115°E–150°E
latr=[15 25];
lonr=[115 150];
latx=lat >= latr(1) & lat <= latr(2);
lonx=lon >= lonr(1) & lon <= lonr(2);
WPlat=lat(latx);
WPlon=lon(lonx);
WPz=z(lonx,latx,:);
WPzm=squeeze(mean(mean(WPz,1),2));
WPx=(WPzm-mean(WPzm))/std(WPzm);
WP.time=WPt;
WP.wpsh=WPx;
%% calc index as in Wang2013 "Subtropical High predictability establishes a promising way for monsoon and tropical storm predictions"
WPix=reshape(WPx,12,[])';
WPt=reshape(WPt,12,[])';
WPy=year(double(WPt(:,1)));
WPix=sum(WPix(:,6:8),2);
WPix=(WPix-nanmean(WPix))/nanstd(WPix);
%plot(WPy,WPix);
%%
WP.yr=WPy;
WP.ix=WPix;
save('WPSHmm','WP')