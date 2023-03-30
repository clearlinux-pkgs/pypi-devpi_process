#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-devpi_process
Version  : 0.3.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/fe/db/d68d9b9313302f304c8ebebb2fc48c78f6c33f269179c9ca59d3e4459546/devpi_process-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fe/db/d68d9b9313302f304c8ebebb2fc48c78f6c33f269179c9ca59d3e4459546/devpi_process-0.3.0.tar.gz
Summary  : devpi process provides a programmatic API to create and use a devpi server process
Group    : Development/Tools
License  : MIT
Requires: pypi-devpi_process-license = %{version}-%{release}
Requires: pypi-devpi_process-python = %{version}-%{release}
Requires: pypi-devpi_process-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# devpi-process
[![PyPI](https://img.shields.io/pypi/v/devpi-process?style=flat-square)](https://pypi.org/project/devpi-process)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/devpi-process?style=flat-square)](https://pypi.org/project/devpi-process)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/devpi-process?style=flat-square)](https://pypi.org/project/devpi-process)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/devpi-process?style=flat-square)](https://pypistats.org/packages/devpi-process)
[![PyPI - License](https://img.shields.io/pypi/l/devpi-process?style=flat-square)](https://opensource.org/licenses/MIT)
[![check](https://github.com/tox-dev/devpi-process/workflows/check/badge.svg)](https://github.com/tox-dev/devpi-process/actions?query=workflow%3Acheck)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

%package license
Summary: license components for the pypi-devpi_process package.
Group: Default

%description license
license components for the pypi-devpi_process package.


%package python
Summary: python components for the pypi-devpi_process package.
Group: Default
Requires: pypi-devpi_process-python3 = %{version}-%{release}

%description python
python components for the pypi-devpi_process package.


%package python3
Summary: python3 components for the pypi-devpi_process package.
Group: Default
Requires: python3-core
Provides: pypi(devpi_process)
Requires: pypi(devpi_client)
Requires: pypi(devpi_server)

%description python3
python3 components for the pypi-devpi_process package.


%prep
%setup -q -n devpi_process-0.3.0
cd %{_builddir}/devpi_process-0.3.0
pushd ..
cp -a devpi_process-0.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680140857
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-devpi_process
cp %{_builddir}/devpi_process-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-devpi_process/e7fd7c458df3ba9633d648e0d666e348689f3559 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-devpi_process/e7fd7c458df3ba9633d648e0d666e348689f3559

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*