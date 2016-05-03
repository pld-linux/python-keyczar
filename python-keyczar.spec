#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	keyczar
Summary:	Toolkit for safe and simple cryptography
Name:		python-%{module}
Version:	0.71c
Release:	3
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://keyczar.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	57154b1e8ad3f59e2c8296d5d5a516eb
URL:		http://www.keyczar.org/
BuildRequires:	python-Crypto
BuildRequires:	python-devel
BuildRequires:	python-pyasn1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-Crypto
Requires:	python-pyasn1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%prep
%setup -q
rm -r python_keyczar.egg-info

%build
%py_build

%if %{with tests}
cd tests/keyczar_tests
PYTHONPATH=$PYTHONPATH:../../src/ ./alltests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc/pycrypt.pdf
%{py_sitescriptdir}/keyczar
%{py_sitescriptdir}/python_keyczar-*.egg-info
