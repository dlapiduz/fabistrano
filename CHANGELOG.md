# Fabistrano changelog

## Unreleased

### Added

- This changelog.
- Ability to avoid using sudo.

### Fixed

- Remove committed `.pyc` files and add `*.pyc` to `.gitignore`.
- Typos in `README.md`.

### Removed

- Unused `VERSION` variable in `fabistrano.deploy`.


## 0.3 - 2013-04-29

### Changed

- Rename `fabistrano.fabistrano` module to `fabistrano.deploy`.
- Change `fabistrano.helpers.dir_exists` to be a no-op.

### Fixed

- Sources package fixed to properly include source files.


## 0.2 - 2013-04-29 [YANKED]

### Changed

- Rename `src` module to `fabistrano`


## 0.1 - 2013-04-28 [YANKED]

### Added

- Initial Release
