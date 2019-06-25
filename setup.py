from setuptools import setup

with open('README.md', 'rb') as f:
    long_description = f.read().decode('utf-8')

setup(
    name='flask_cc_wechat',
    version='0.1.1',
    description="Flask wechat expansion development",
    long_description=long_description,
    license='BSD',
    author='wen',
    author_email='w_angzhiwen@163.com',
    packages=['flask_cc_wechat'],
    install_requires=[
        'Flask',
        'requests'
    ],
    zip_safe=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
