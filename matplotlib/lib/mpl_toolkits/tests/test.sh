cd ../../../
sudo rm -rf cover
python tests.py --with-coverage --cover-html --cover-branch --cover-package=mpl_toolkits.mplot3d.axes3d mpl_toolkits.tests.test_errorbar3 mpl_toolkits.tests.test_errorbar2 mpl_toolkits.tests.test_errorbar1

