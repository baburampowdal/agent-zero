from python.helpers.api import ApiHandler
from flask import Request, Response, send_file

from python.helpers.file_browser import FileBrowser
from python.helpers import files
import os




class DownloadWorkDirFile(ApiHandler):
    async def process(self, input: dict, request: Request) -> dict | Response:
        file_path = request.args.get('path', '')
        if not file_path:
            raise ValueError("No file path provided")
            
        work_dir = files.get_abs_path("work_dir")
        browser = FileBrowser(work_dir)
        
        full_path = browser.get_file_path(file_path)
        if full_path:
            return send_file(
                full_path, 
                as_attachment=True,
                download_name=os.path.basename(file_path)
            )
        raise Exception("File not found")