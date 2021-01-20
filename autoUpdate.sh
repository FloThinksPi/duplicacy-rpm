#!/bin/bash

author="Florian Braun"

# From https://stackoverflow.com/questions/4023830/how-to-compare-two-strings-in-dot-separated-version-format-in-bash
verlte() {
    [  "$1" = "`echo -e "$1\n$2" | sort -V | head -n1`" ]
}
verlt() {
    [ "$1" = "$2" ] && return 1 || verlte $1 $2
}
isver() {
  [[ $1 =~ ^[0-9]+\.[0-9]+ ]]
}
# End From

newestVersion=$(curl --silent "https://api.github.com/repos/gilbertchen/duplicacy/releases/latest" | jq -r .tag_name | tail -c +2)
currentVersion=$(grep -e "Version: *[0-9\.]*" duplicacy.spec | tail -c +10)

echo "Current Version is $currentVersion and newest is $newestVersion"

if ! isver $newestVersion
then
  echo "New version is not a Version"
  exit 1
fi

if verlt $currentVersion $newestVersion
  then
    echo "I am going to update the package."
    sed -i "0,/Version: [0-9/.]*/{s/Version: [0-9/.]*/Version: $newestVersion/}" duplicacy.spec
    sed -i '0,/Release: [0-9]*/{s/Release: [0-9]*/Release: 1/}' duplicacy.spec
    changelog=$(printf "* ";LANG=en_us_88591; echo -n `date +'%a %b %d %Y'`; printf " $author - $newestVersion\n"; curl --silent "https://api.github.com/repos/gilbertchen/duplicacy/releases/latest" | jq -r .body | sed 's/^\*/-/g')
    awk -v changelog="\n$changelog\n" '{print} /%changelog/{print changelog}' duplicacy.spec > tmp && mv tmp duplicacy.spec
    make update-sources
    git commit -m "Updated Package from Version $currentVersion to $newestVersion" duplicacy.spec sources
  else
    echo "Nothing to do."
fi
