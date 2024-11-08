import os
from typing import List, Optional
from hfutils.archive.base import archive_unpack
from hfutils.index.make import tar_create_index
from hfutils.index.local_fetch import (
    tar_get_index, tar_list_files, tar_file_exists, tar_file_size, 
    tar_file_info, tar_file_download
)
from tarfile import TarFile

__all__ = [
    "pack_directory_to_tarfile", 
    "unpack_tarfile", 
    "create_index_from_tarfile", 
    "create_tarfile_index_for_directory",
    "get_tarfile_index", 
    "list_files_in_tarfile", 
    "is_file_in_tarfile", 
    "get_file_size_in_tarfile",
    "get_file_info_in_tarfile", 
    "export_file_from_tarfile"
]

def pack_directory_to_tarfile(
    src_directory: str, 
    archive_file: Optional[str] = None, 
    pattern: Optional[str] = None, 
    silent: bool = False
) -> str:
    """Pack a directory into a tar file
    
    Args:
        src_directory: Source directory path
        archive_file: Target tar file path, defaults to {directory_name}.tar in current directory
        pattern: File patterns to exclude, separated by semicolons
        silent: Whether to run in silent mode
    
    Returns:
        str: Path to the generated tar file
    """
    if archive_file is None:
        archive_file = os.path.join(os.getcwd(), f"{os.path.basename(src_directory)}.tar")
    
    os.makedirs(os.path.dirname(archive_file), exist_ok=True)
    
    with TarFile.open(archive_file, "w") as tar:
        for root, _, files in os.walk(src_directory):
            for file in files:
                if pattern:
                    pattern_list = [p.strip() for p in pattern.split(";") if p.strip()]
                    if pattern_list and any(file.endswith(p) for p in pattern_list):
                        continue
                file_path = os.path.join(root, file)
                tar.add(file_path, arcname=os.path.relpath(file_path, src_directory))
    
    return archive_file

def unpack_tarfile(
    archive_file: str, 
    directory: str = None, 
    silent: bool = False
) -> str:
    """Unpack a tar file to a directory
    
    Args:
        archive_file: Path to the tar file
        directory: Target directory path, defaults to current directory
        silent: Whether to run in silent mode
    
    Returns:
        str: Path to the unpacked directory
    """
    if directory is None:
        directory = os.getcwd()
    directory = os.path.join(directory, os.path.basename(archive_file))
    return archive_unpack(archive_file, directory, silent)

def create_index_from_tarfile(
    archive_file: str, 
    index_file_path: str = None, 
    silent: bool = False
) -> str:
    """Create an index file from a tar file
    
    Args:
        archive_file: Path to the tar file
        index_file_path: Path to the index file, defaults to tar file name with .json extension
        silent: Whether to run in silent mode
    
    Returns:
        str: Path to the created index file
    """
    if index_file_path is None:
        index_file_path = archive_file.replace(".tar", ".json")
    return tar_create_index(archive_file, index_file_path, silent)

def create_tarfile_index_for_directory(
    src_directory: str, 
    archive_file: str | None = None, 
    index_file_path: str | None = None, 
    pattern: str | None = None, 
    silent: bool = False
) -> str:
    """Create a tar file index for a directory
    
    Args:
        src_directory: Source directory path
        archive_file: Target tar file path, defaults to {directory_name}.tar in current directory
        index_file_path: Path to the index file, defaults to tar file name with .json extension
        pattern: File patterns to exclude, separated by semicolons
        silent: Whether to run in silent mode
    
    Returns:
        str: Path to the created index file
    """
    pack_directory_to_tarfile(src_directory, archive_file, pattern, silent=silent)
    create_index_from_tarfile(archive_file, index_file_path, silent=silent)

def get_file_size_in_tarfile(
    archive_file: str, 
    file_in_archive: str, 
    idx_file_path: Optional[str] = None
) -> int:
    """Get the size of a specified file in the tar archive
    
    Args:
        archive_file: Path to the tar file
        file_in_archive: Path of the file within the tar archive
        idx_file_path: Path to the index file, defaults to tar file name with .json extension
        
    Returns:
        int: File size in bytes
    """
    if idx_file_path is None:
        idx_file_path = get_default_index_path(archive_file)
    return tar_file_size(archive_file, file_in_archive, idx_file_path)

def get_file_info_in_tarfile(
    archive_file: str, 
    file_in_archive: str, 
    idx_file_path: str | None = None
) -> dict:
    """Get the information of a specified file in the tar archive

    Args:
        archive_file: Path to the tar file
        file_in_archive: Path of the file within the tar archive
        idx_file_path: Path to the index file, defaults to tar file name with .json extension
    
    Returns:
        dict: File information
    """
    if idx_file_path is None:
        idx_file_path = archive_file.replace(".tar", ".json")
    return tar_file_info(archive_file, file_in_archive, idx_file_path)

def get_tarfile_index(
    archive_file: str, 
    idx_file_path: str | None = None
) -> dict:
    """Get the index of a tar file
    
    Args:
        archive_file: Path to the tar file
        idx_file_path: Path to the index file, defaults to tar file name with .json extension
    
    Returns:
        dict: Index information
    """
    if idx_file_path is None:
        idx_file_path = archive_file.replace(".tar", ".json")
    return tar_get_index(archive_file, idx_file_path)

def export_file_from_tarfile(
    archive_file: str, 
    file_in_archive: str, 
    local_file: str, 
    idx_file_path: Optional[str] = None, 
    chunk_size: int = 1048576, 
    force_download: bool = False
) -> bool:
    """Export a specific file from the tar archive
    
    Args:
        archive_file: Path to the tar file
        file_in_archive: Path of the file to export from the archive
        local_file: Target path for the exported file
        idx_file_path: Path to the index file
        chunk_size: Size of chunks for reading
        force_download: Whether to force download even if file exists
        
    Returns:
        bool: Whether the export was successful
    """
    if idx_file_path is None:
        idx_file_path = get_default_index_path(archive_file)
    return tar_file_download(
        archive_file, 
        file_in_archive, 
        local_file, 
        idx_file_path, 
        chunk_size, 
        force_download
    )

def list_files_in_tarfile(
    archive_file: str, 
    idx_file_path: str | None = None
) -> List[str]:
    """List all files in a tar file
    
    Args:
        archive_file: Path to the tar file
        idx_file_path: Path to the index file, defaults to tar file name with .json extension
    
    Returns:
        List[str]: List of file paths
    """
    if idx_file_path is None:
        idx_file_path = archive_file.replace(".tar", ".json")
    return tar_list_files(archive_file, idx_file_path)

def is_file_in_tarfile(
    archive_file: str, 
    file_in_archive: str, 
    idx_file_path: str | None = None
) -> bool:
    """Check if a file exists in a tar file
    
    Args:
        archive_file: Path to the tar file
        file_in_archive: Path of the file within the tar archive
        idx_file_path: Path to the index file, defaults to tar file name with .json extension
    
    Returns:
        bool: Whether the file exists
    """
    if idx_file_path is None:
        idx_file_path = archive_file.replace(".tar", ".json")
    return tar_file_exists(archive_file, file_in_archive, idx_file_path)

def get_default_index_path(
    archive_file: str
) -> str:
    """Get the default index file path
    
    Args:
        archive_file: Path to the tar file
        
    Returns:
        str: Corresponding index file path
    """
    return archive_file.replace(".tar", ".json")