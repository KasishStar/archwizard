pkgname=archwizard
pkgver=0.1.1
pkgrel=1
pkgdesc="A simple setup wizard for Arch Linux"
arch=('any')
url="https://github.com/KasishStar/ArchWizard"
license=('MIT')

depends=(
'python'
)

makedepends=(
'python-build'
'python-installer'
'python-setuptools'
)

source=(
"$pkgname-$pkgver.tar.gz::https://github.com/KasishStar/ArchWizard/archive/refs/tags/v$pkgver.tar.gz"
)

sha256sums=('6ae0c25acebf72a25c4d2e06097a26b5174cd76897d59de3c0196c6cc3a89666')

build() {
cd "$srcdir/$pkgname-$pkgver"
python -m build --wheel --no-isolation
}

package() {
cd "$srcdir/$pkgname-$pkgver"

```
python -m installer \
    --destdir="$pkgdir" \
    dist/*.whl

install -Dm644 LICENSE \
    "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
```

}
