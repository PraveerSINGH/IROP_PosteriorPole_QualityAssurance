from setuptools import setup, find_packages

setup(
    name='qtim_ROP',
    packages=find_packages(),
    version='0.4',
    description = 'A package for segmentation and classification of retinal images',
    entry_points = {
        "console_scripts": ['deeprop = qtim_ROP.__main__:main']
    },
    author='James Brown',
    author_email='jbrown97@mgh.harvard.edu',
    url='https://github.com/QTIM-Lab/qtim_ROP',
    download_url = 'https://github.com/QTIM-Lab/qtim_ROP/tarball/0.2',
    keywords=['retina', 'retinopathy of prematurity', 'plus disease', 'machine learning', 'deep learning', 'CNN'],
    install_requires=['tensorflow==1.8', 'opencv-python', 'SimpleITK', 'addict', 'appdirs', 'pandas>=0.21.0', 'seaborn', 'matplotlib', 'keras==2.1.6',
                      'h5py', 'scikit-learn', 'scikit-image==0.13.0'],
    extras_require={
            'gpu_support':  ["tensorflow"]
    },
    package_data={'qtim_ROP': ['config/preprocessing.yaml']},
    classifiers=[],
)
