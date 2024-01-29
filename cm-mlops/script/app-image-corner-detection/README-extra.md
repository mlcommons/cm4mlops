# Examples

```bash
cm run script "app image corner-detection"
cm run script "app image corner-detection" -add_deps_recursive.compiler.tags=llvm
cm run script "app image corner-detection" -add_deps_recursive.compiler.tags=gcc
cm run script "app image corner-detection" -add_deps_recursive.compiler.tags=llvm --add_deps_recursive.compiler.version_min=11.0.0 --add_deps_recursive.compiler.version_max=13.0.0
```

## Reproducibility matrix

* Ubuntu 22.04; x64; LLVM 17.06
* Windows 11; x64; LLVM 17.06

