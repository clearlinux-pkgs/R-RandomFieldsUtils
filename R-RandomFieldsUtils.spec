#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RandomFieldsUtils
Version  : 1.2.5
Release  : 54
URL      : https://cran.r-project.org/src/contrib/RandomFieldsUtils_1.2.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RandomFieldsUtils_1.2.5.tar.gz
Summary  : Utilities for the Simulation and Analysis of Random Fields and
Group    : Development/Tools
License  : GPL-3.0
Requires: R-RandomFieldsUtils-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-RandomFieldsUtils package.
Group: Libraries

%description lib
lib components for the R-RandomFieldsUtils package.


%prep
%setup -q -c -n RandomFieldsUtils
cd %{_builddir}/RandomFieldsUtils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650387106

%install
export SOURCE_DATE_EPOCH=1650387106
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RandomFieldsUtils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RandomFieldsUtils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RandomFieldsUtils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RandomFieldsUtils || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RandomFieldsUtils/CITATION
/usr/lib64/R/library/RandomFieldsUtils/DESCRIPTION
/usr/lib64/R/library/RandomFieldsUtils/INDEX
/usr/lib64/R/library/RandomFieldsUtils/Meta/Rd.rds
/usr/lib64/R/library/RandomFieldsUtils/Meta/features.rds
/usr/lib64/R/library/RandomFieldsUtils/Meta/hsearch.rds
/usr/lib64/R/library/RandomFieldsUtils/Meta/links.rds
/usr/lib64/R/library/RandomFieldsUtils/Meta/nsInfo.rds
/usr/lib64/R/library/RandomFieldsUtils/Meta/package.rds
/usr/lib64/R/library/RandomFieldsUtils/NAMESPACE
/usr/lib64/R/library/RandomFieldsUtils/R/RandomFieldsUtils
/usr/lib64/R/library/RandomFieldsUtils/R/RandomFieldsUtils.rdb
/usr/lib64/R/library/RandomFieldsUtils/R/RandomFieldsUtils.rdx
/usr/lib64/R/library/RandomFieldsUtils/help/AnIndex
/usr/lib64/R/library/RandomFieldsUtils/help/RandomFieldsUtils.rdb
/usr/lib64/R/library/RandomFieldsUtils/help/RandomFieldsUtils.rdx
/usr/lib64/R/library/RandomFieldsUtils/help/aliases.rds
/usr/lib64/R/library/RandomFieldsUtils/help/macros/allg_defn.Rd
/usr/lib64/R/library/RandomFieldsUtils/help/paths.rds
/usr/lib64/R/library/RandomFieldsUtils/html/00Index.html
/usr/lib64/R/library/RandomFieldsUtils/html/R.css
/usr/lib64/R/library/RandomFieldsUtils/include/AutoRandomFieldsUtils.h
/usr/lib64/R/library/RandomFieldsUtils/include/AutoRandomFieldsUtilsLocal.h
/usr/lib64/R/library/RandomFieldsUtils/include/Basic_utils.h
/usr/lib64/R/library/RandomFieldsUtils/include/Basic_utils_local.h
/usr/lib64/R/library/RandomFieldsUtils/include/General_utils.h
/usr/lib64/R/library/RandomFieldsUtils/include/RFU.h
/usr/lib64/R/library/RandomFieldsUtils/include/RandomFieldsUtils.h
/usr/lib64/R/library/RandomFieldsUtils/include/Utils.h
/usr/lib64/R/library/RandomFieldsUtils/include/def.h
/usr/lib64/R/library/RandomFieldsUtils/include/errors_messages.h
/usr/lib64/R/library/RandomFieldsUtils/include/extern.h
/usr/lib64/R/library/RandomFieldsUtils/include/intrinsics.h
/usr/lib64/R/library/RandomFieldsUtils/include/kleinkram.h
/usr/lib64/R/library/RandomFieldsUtils/include/options.h
/usr/lib64/R/library/RandomFieldsUtils/include/parallel_base.h
/usr/lib64/R/library/RandomFieldsUtils/include/parallel_simd.h
/usr/lib64/R/library/RandomFieldsUtils/include/solve_gpu.h
/usr/lib64/R/library/RandomFieldsUtils/include/sse2neon.h
/usr/lib64/R/library/RandomFieldsUtils/include/win_linux_aux.h
/usr/lib64/R/library/RandomFieldsUtils/include/xport_import.h
/usr/lib64/R/library/RandomFieldsUtils/include/zzz_RandomFieldsUtils.h
/usr/lib64/R/library/RandomFieldsUtils/include/zzz_calls.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RandomFieldsUtils/libs/RandomFieldsUtils.so
/usr/lib64/R/library/RandomFieldsUtils/libs/RandomFieldsUtils.so.avx2
/usr/lib64/R/library/RandomFieldsUtils/libs/RandomFieldsUtils.so.avx512
