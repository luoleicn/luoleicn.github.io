cd /root/luoleicn.github.io &&\
git pull &&\
jekyll build &&\
rm /etc/nginx/html/* -rf &&\
cp -r _site/* /etc/nginx/html/ &&\
rm -rf _site



