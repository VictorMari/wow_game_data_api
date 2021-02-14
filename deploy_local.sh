LOCAL_MODULES="/home/labosis/.local/lib/python3.9/site-packages"
MODULE_NAME="wow_game_data_api"
MODULE_PATH="/home/labosis/Projects/wow_game_data_api"
REMOTE_URL="git@gitlab.home.com:labosis/wow_game_data_api.git"

sudo rm -r /tmp/$MODULE_NAME
mkdir /tmp/$MODULE_NAME
pushd /tmp/$MODULE_NAME 
git init .
git remote add local $REMOTE_URL
git pull local master
sudo rm -rf .git 

cd ..
rm -rf $LOCAL_MODULES/$MODULE_NAME
cp -r $MODULE_NAME $LOCAL_MODULES/$MODULE_NAME
echo "Moved files to local site packages"

