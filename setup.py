from setuptools import setup, find_packages

setup(
    author='Luke Hollis',
    author_email='luke@lukehollis.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ],
    description=(''),
    # find actual keywords in future
    keywords=['literature', 'philology', 'text processing', 'archive'],
    license='MIT',
    long_description="""Open Words is an open source initiative to modernize William Whitaker's 'Whitaker's Words' program so that it may continue to be useful to Latin students and philologists for years to come.""",
    name='open_words',
    packages=find_packages(),
    url='https://github.com/segetes/open_words',
    version='0.01',
    zip_safe=True,
)
