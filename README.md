## Persistence et bases de données

Ce cours porte sur les bases de donneés relationnelles

Site du cours : http://oci.donner-online.ch/poo/

*   version PDF : http://oci.donner-online.ch/poo/_downloads/oci-chap-poo.pdf


# Building the course on gitpod

Visit http://gitpod.io#https://github.com/oci1517/files-db and run following commands in the Terminal

```bash
pipenv shell
pipenv install
make youtube-patch
make html
```

This builds the course from the RestructuredText sources. To serve the content, use the one of the commands

*   `make livehtml` and open the preview in the browser (optionally open the port to public)
*   `make livecorrige` to view the solutions to view the version of the website with the solutions to the exercises     and open the preview in the browser (optionally open the port to public)

