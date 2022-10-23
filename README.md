<p align="center">
  <a href="https://wagtail.org/">
    <img alt="Wagtail" src="https://wagtail.org/static/img/wagtail.dbf60545a188.svg" width="100" />
  </a>
</p>

<h1 align="center">
  Aurore Wagtail CMS Starter
</h1>

<p align="center">
Medusa is an open-source headless commerce engine that enables developers to create amazing digital commerce experiences. This CMS backend is used to illustrate how it can be integrated with Medusa Next.JS starter.
</p>

> **Prerequisites**: To use the starter you should have [Python 3](https://www.python.org/downloads/).

# Overview

![aurore-cover](https://github.com/traleor/aurore-frontend/blob/main/public/cover.png)

Aurore is a Multi-vendor marketplace built using Medusa, Wagtail for the CMS and Next.Js for the Front-end.
This marketplace is easy to maintain and update to the latest Medusa version as it is built entirely with the tools provided by Medusa (no third-party included).

## Participants:

<!-- markdown table with the team infos -->

| Name        | Github                                   | Twitter                                      | Discord              |
| ----------- | ---------------------------------------- | -------------------------------------------- | -------------------- |
| Peng Boris  | [Github](https://github.com/itzomen)     | [Twitter](https://twitter.com/itz_omen)      | `itzomen#4530`       |
| Njoh Prince | [Github](https://github.com/NjohPrince)  | [Twitter](https://twitter.com/NjohNoh)       | `theunicorndev#2216` |
| Egbe Nesta  | [Github](https://github.com/nestaenow)   | [Twitter](https://twitter.com/nestaenow)     | `NestaEnow#4271`     |
| Meli Imelda | [Github](https://github.com/meli-imelda) | [Twitter](https://twitter.com/Meli_Tchouala) | `MeliImelda#2152`    |

The Aurore CMS backend is built with:

- [Django 3](https://wagtail.org/)
- [wagtail CMS](https://www.djangoproject.com/)

# Quickstart

## [Demo](https://aurore-cms.herokuapp.com/cms)

> Email: `admin@email.com`

> Password: `password`

## Setup

1. Clone the repository

```bash
git clone https://github.com/traleor/aurore-wagtail.git
```

2. Install dependencies

```bash
cd aurore-wagtail
pip install -r requirements.txt
```

3. Create a `.env` file and add the following environment variables:

```bash
# use .env.example as a reference
SECRET_KEY=your-secret-key
DEBUG=True
```

4. Run migrations

```bash

python manage.py migrate
```

5. Create a superuser

```bash
python manage.py createsuperuser
```

6. Run the development server

```bash
python manage.py runserver
```

7. Open [http://localhost:8000](http://localhost:8000) and start editing the site!
