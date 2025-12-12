%define oname appdirs

Name:		python-%{oname}
Version:	1.4.4
Release:	5
Summary:	A small Python module for determining appropriate platform-specific dirs
Source0:	https://github.com/ActiveState/appdirs/archive/%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/ActiveState/appdirs
BuildArch:	noarch
BuildRequires:	python3dist(setuptools)

%description
What directory should your app use for storing user data?

This kind of thing is what the ``appdirs`` module is for.
``appdirs`` will help you choose an appropriate:

- user data dir (``user_data_dir``)
- user config dir (``user_config_dir``)
- user cache dir (``user_cache_dir``)
- site data dir (``site_data_dir``)
- site config dir (``site_config_dir``)
- user log dir (``user_log_dir``)

and also:

- is a single module so other Python packages can include their own
  private copy
- is slightly opinionated on the directory names used. Look for "OPINION" in
  documentation and code for when an opinion is being applied.

%prep
%autosetup -n %{oname}-%{version}

%build
%py3_build

%install
%py3_install

%check
python setup.py test

%files
%doc CHANGES.rst
%doc LICENSE.txt
%doc README.rst
%{py_puresitedir}/appdirs.py*
%{py_puresitedir}/appdirs*.egg-info
