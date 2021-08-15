# copier

Copy your credentials more easy.

## Installation

To install use the `install.sh` script:

```sh
curl -sL https://raw.githubusercontent.com/AlphaTechnolog/copier/master/bin/install.sh | bash
```

## Uninstall

To uninstall use the `uninstall.sh` script:

```sh
curl -sL https://raw.githubusercontent.com/AlphaTechnolog/copier/master/bin/uninstall.sh | bash
```

## Concepts explain

Copier save your credentials on your local machine, it works offline.

The file of the storage is in `~/.copierrc.json`, check an example .copierrc.json file:

```json
{
    "credentials": {
        "mail_password": "MAIL_PASSWORD"
    }
}
```

## Getting started

See the next steps to get started with
copier.

### Creating credentials

First create your credential:

```sh
copier config create -k mail_password -v MAIL_PASSWORD
```

Now check the config content:

```sh
copier config
```

It shows:

```
credentials:
  mail_password: MAIL_PASSWORD
```

If you cat ~/.copierrrc.json, you get:

```json
{"credentials": {"mail_password": "MAIL_PASSWORD"}}
```

> Same of `copier config` output

### Copying credentials

Now we have a credential named: `mail_password`, copy it with
copier!:

```sh
copier -c mail_password
```

It shows:

```
Copying to your clipboard...
Copied successfully to your clipboard, try using Ctrl-Shift-V on your terminal to paste it!
```

## Enjoy

Thanks for use copier, this script
was created with python and love!