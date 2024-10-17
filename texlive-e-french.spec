Name:		texlive-e-french
Version:	52027
Release:	2
Summary:	Comprehensive LaTeX support for French-language typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/e-french
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/e-french.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/e-french.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
E-french is a distribution that keeps alive the work of Bernard
Gaulle (now deceased), under a free licence. It replaces the
old "full" frenchpro (the "professional" distribution) and the
light-weight frenchle packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/e-french
%{_texmfdistdir}/makeindex/e-french
%doc %{_texmfdistdir}/doc/generic/e-french

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
