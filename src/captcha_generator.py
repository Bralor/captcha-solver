import os
import logging

from src.generator_honza import MyImageCaptcha

from captcha.image import ImageCaptcha


class DatasetGenerator:
    """Create a set of files"""

    def __init__(
            self,
            size_x: int,
            size_y: int,
            content: str,
            folder: str = ""
    ):
        self.size_x = size_x
        self.size_y = size_y
        self.folder = folder
        self.content = content

        self.logger = self.set_logging()
        self.create_empty_dir(self.logger)


    def set_logging(self) -> logging.Logger:
        """
        Initiate the logging inside the module.
        """
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        log_handler = logging.FileHandler("runtime_logs.log")
        log_format = logging.Formatter(
            "[ %(asctime)s ] - [%(name)s-%(lineno)d] - %(message)s"
        )
        log_handler.setFormatter(log_format)
        logger.addHandler(log_handler)

        return logger


    def create_empty_dir(self, log) -> None:
        """
        Create an empty directory if it does not already exist.

        :Example:
        >>> dataset_1 = DatasetGenerator(
        ...     size_x=180,
        ...     size_y=50,
        ...     folder="images",
        ...     content="a1bc2"
        ... )
        >>> dataset_1.create_empty_dir()
        INFO: created directory 'images' in the root.
        """
        try:
            os.mkdir(self.folder)

        except FileExistsError:
            log.warning(f"WARNING: Folder '{self.folder}' already exists.")
        else:
            log.info(f"INFO: created directory '{self.folder}' in the root.")


    def generate_dataset(self, root_dir: str):
        """
        Create a dataset of captcha images.

        :Example:
        >>> dataset_1 = DatasetGenerator(
        ...     size_x=180, size_y=50, choices=5, content="a1bc2"
        ... )
        >>> dataset_1.generate_dataset()
        INFO: created directory /captcha_solver/images/ ..
        INFO: generated dataset of 5 images in /captcha_solver/images/*.
        """
        status: str = self.create_empty_dir(root_dir)

        if status.startswith("INFO:") or status.startswith("WARNING:"):
            return self.create_image(root_dir, self.content)


    def create_image(self, root_dir: str) -> None:
        """
        Create image object and save it to the disc.

        :return: the string with the name of .png file
        :rtype: str
        """
        # image = MyImageCaptcha(self.size_x, self.size_y)
        image = ImageCaptcha(fonts=["DroidSansMono.ttf"])
        data = image.generate(self.content)
        image.write(
            self.content,
            os.path.join(self.folder, f"{self.content}.png")
        )





