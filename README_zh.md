# shiertier_tar

[English](https://github.com/shiertier-utils/shiertier_tar/blob/main/README.md) | 中文

## 简介

`shiertier_tar` 是一个 Python 库，旨在简化与 tar 归档文件的工作过程。它提供了一组实用函数，用于将目录打包到 tar 文件中、解压 tar 文件、创建和管理 tar 文件索引，以及对 tar 文件执行各种操作。该库特别适用于以结构化方式管理大型数据集或归档文件。

## 安装

您可以通过 `pip` 安装 `shiertier_tar`：

```bash
pip install shiertier_tar
```

请注意，该项目仍在开发中。

## 使用方法

### 将目录打包到 Tar 文件

您可以使用 `pack_directory_to_tarfile` 函数将目录打包到 tar 文件中。该函数允许您指定源目录、可选的归档文件名和用于过滤文件的模式。

```python
from shiertier_tar import pack_directory_to_tarfile

# 将目录打包到 tar 文件
pack_directory_to_tarfile(src_directory='path/to/source_directory', archive_file='path/to/archive.tar', pattern='*.txt;*.md')
```

### 解压 Tar 文件

您可以使用 `unpack_tarfile` 函数解压 tar 文件。该函数允许您指定 tar 文件和可选的目标目录。

```python
from shiertier_tar import unpack_tarfile

# 解压 tar 文件
unpack_tarfile(archive_file='path/to/archive.tar', directory='path/to/destination_directory')
```

### 从 Tar 文件创建索引

您可以使用 `create_index_from_tarfile` 函数从 tar 文件创建索引。该函数允许您指定 tar 文件和可选的索引目录。

```python
from shiertier_tar import create_index_from_tarfile

# 从 tar 文件创建索引
create_index_from_tarfile(archive_file='path/to/archive.tar', directory='path/to/index_directory')
```

### 为目录创建 Tar 文件索引

您可以使用 `create_tarfile_index_for_directory` 函数为目录创建 tar 文件索引。该函数允许您指定源目录、可选的归档文件名、可选的索引目录和用于过滤文件的模式。

```python
from shiertier_tar import create_tarfile_index_for_directory

# 为目录创建 tar 文件索引
create_tarfile_index_for_directory(src_directory='path/to/source_directory', archive_file='path/to/archive.tar', index_directory='path/to/index_directory', pattern='*.txt;*.md')
```

### 列出 Tar 文件中的文件

您可以使用 `list_files_in_tarfile` 函数列出 tar 文件中的文件。该函数允许您指定 tar 文件和可选的索引文件。

```python
from shiertier_tar import list_files_in_tarfile

# 列出 tar 文件中的文件
files = list_files_in_tarfile(archive_file='path/to/archive.tar')
print(files)
```

### 检查文件是否存在于 Tar 文件中

您可以使用 `is_file_in_tarfile` 函数检查文件是否存在于 tar 文件中。该函数允许您指定 tar 文件、归档文件中的文件和可选的索引文件。

```python
from shiertier_tar import is_file_in_tarfile

# 检查文件是否存在于 tar 文件中
exists = is_file_in_tarfile(archive_file='path/to/archive.tar', file_in_archive='file_in_archive.txt')
print(exists)
```

### 获取 Tar 文件中文件的大小

您可以使用 `get_file_size_in_tarfile` 函数获取 tar 文件中文件的大小。该函数允许您指定 tar 文件、归档文件中的文件和可选的索引文件。

```python
from shiertier_tar import get_file_size_in_tarfile

# 获取 tar 文件中文件的大小
size = get_file_size_in_tarfile(archive_file='path/to/archive.tar', file_in_archive='file_in_archive.txt')
print(size)
```

### 获取 Tar 文件中文件的信息

您可以使用 `get_file_info_in_tarfile` 函数获取 tar 文件中文件的信息。该函数允许您指定 tar 文件、归档文件中的文件和可选的索引文件。

```python
from shiertier_tar import get_file_info_in_tarfile

# 获取 tar 文件中文件的信息
info = get_file_info_in_tarfile(archive_file='path/to/archive.tar', file_in_archive='file_in_archive.txt')
print(info)
```

### 从 Tar 文件导出文件

您可以使用 `export_file_from_tarfile` 函数从 tar 文件导出文件。该函数允许您指定 tar 文件、归档文件中的文件、本地文件路径、可选的索引文件和可选的块大小。

```python
from shiertier_tar import export_file_from_tarfile

# 从 tar 文件导出文件
export_file_from_tarfile(archive_file='path/to/archive.tar', file_in_archive='file_in_archive.txt', local_file='path/to/local_file.txt')
```

## 依赖

- `hfutils`

## 许可证

本项目基于 MIT 许可证发布。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。