from distutils.core import setup
setup(
  name = 'bitscraper',
  packages = ['bitscraper'],
  version = '0.1',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Access data of products (stocks, futures,etc...) from the italian stock market (Borsa Italiana)',
  author = 'Federico Pizzolo',
  author_email = 'federicopizzolo@gmail.com',
  url = 'https://github.com/shatteringlass/bit_scraper',
  download_url = 'https://github.com/shatteringlass/bit_scraper/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['stock', 'market', 'italy', 'borsa', 'italiana', 'milano', 'mib'],
  install_requires=[
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)