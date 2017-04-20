#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	keyczar
Summary:	Toolkit for safe and simple cryptography
Summary(pl.UTF-8):	Zbiór narzędzi do bezpiecznej i prostej kryptografii
Name:		python-%{module}
Version:	0.716
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
# github tarballs contain all bindings, regardless of tag kind...
##Source0Download: https://github.com/google/keyczar/releases
#Source0:	https://github.com/google/keyczar/archive/Python_release_%{version}.tar.gz
# ...so use pypi tarball
#Source0Download: https://pypi.python.org/simple/python-keyczar
Source0:	https://files.pythonhosted.org/packages/source/p/python-keyczar/%{name}-%{version}.tar.gz
# Source0-md5:	734334a6c5921e39003b68429eee77ae
Patch0:		%{name}-tests.patch
URL:		http://www.keyczar.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Crypto
BuildRequires:	python-pyasn1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%description -l pl.UTF-8
Keyczar to mający otwarte źródła zbiór narzędzi kryptograficznych
zaprojektowany tak, aby programiści mogli łatwiej i bezpieczniej
wykorzystywać kryptografię w swoich aplikacjach. Keyczar obsługuje
uwierzytelnianie oraz szyfrowanie z kluczami symetrycznymi oraz
asymetrycznymi.

%prep
%setup -q
%patch0 -p1

%{__rm} -r python_keyczar.egg-info

%build
%py_build

%if %{with tests}
srcdir=$(pwd)/src
# scripts expect data in ../../testdata, so run them from this subdir
cd tests/keyczar_tests
PYTHONPATH=${srcdir} %{__python} alltests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/pycrypt.pdf
%attr(755,root,root) %{_bindir}/keyczart
%{py_sitescriptdir}/keyczar
%{py_sitescriptdir}/python_keyczar-*.egg-info
