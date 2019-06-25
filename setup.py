from setuptools import setup

setup(
    name='flask_cc_wechat',
    version='0.1',
    description="Flask wechat expansion development",
    long_description=__doc__,
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
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
