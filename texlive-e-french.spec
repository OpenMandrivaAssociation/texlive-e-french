%global tl_name e-french
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.11
Release:	%{tl_revision}.1
Summary:	Comprehensive LaTeX support for French-language typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/french/e-french
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/e-french.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/e-french.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
E-french is a distribution that keeps alive the work of Bernard Gaulle
(now deceased), under a free licence. It replaces the old "full"
frenchpro (the "professional" distribution) and the light-weight
frenchle packages.

