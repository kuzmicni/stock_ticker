from setuptools import setup, find_packages

setup(
    name="stock_ticker",
    version="0.1.0",
    description="CLI to fetch YTD stock performance",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "click",
        "yfinance"
    ],
    entry_points={
        'console_scripts': [
            'stock_ticker=stock_ticker.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
