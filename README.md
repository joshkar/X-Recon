<h1 align="center">
  <br>
  <a href="https://github.com/joshkar/X-Recon"><img src=".imgs/banner.jpg" alt="X-Recon"></a>

</h1>

<h4 align="center">A tool to find web page inputs and perform XSS scanning.</h4>

<p align="center">

  <a href="http://python.org">
    <img src="https://img.shields.io/badge/python-v3-blue">
  </a>

  <a href="https://en.wikipedia.org/wiki/Linux">
    <img src="https://img.shields.io/badge/Platform-Linux-red">
  </a>

</p>

### Features:
- **Subdomain Discovery:**
  - Fetches relevant subdomains for the target website and compiles them into a whitelist. These subdomains can be utilized during the scraping process.

- **Site-wide Link Discovery:**
  - Gathers all links across the website based on the provided whitelist and the specified `max_depth`.

- **Form and Input Extraction:**
  - Identifies all forms and inputs found within the extracted links, creating a JSON output. This JSON output serves as a foundation for leveraging the XSS scanning capability of the tool.

<br>

![demo](.imgs/demo1.jpg)