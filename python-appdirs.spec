%define	oname	appdirs

Name:		python-%{oname}
Version:	1.4.4
Release:	1
Summary:	A small Python module for determining appropriate platform-specific dirs
Source0:	https://github.com/ActiveState/appdirs/archive/%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://github.com/ActiveState/appdirs
BuildArch:	noarch
BuildRequires:	python3egg(setuptools)
BuildRequires:	pythonegg(setuptools)

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

%package -n python2-%{oname}
Summary:        small Python module for determining appropriate platform-specific dirs
Group:          Development/Python

%description -n python2-%{oname}
Python2 module for determining appropriate platform-specific dirs.

%prep
%setup -q -n %{oname}-%{version}
cp -a . %{py3dir}

%build
%{__python2} setup.py build
cd %{py3dir}
%{__python3} setup.py build
cd -

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
cd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
cd -

%check
python setup.py test

%files
%doc CHANGES.rst
%doc LICENSE.txt
%doc README.rst
%{py_puresitedir}/appdirs.py*
%{py_puresitedir}/appdirs*.egg-info
%{py_puresitedir}/__pycache__/appdirs.cpython*

%files -n python2-%{oname}
%{py2_puresitedir}/appdirs.py*
%{py2_puresitedir}/appdirs*.egg-info
