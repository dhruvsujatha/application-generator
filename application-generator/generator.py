#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from pathlib import Path

import jinja2
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Build path to template folder form root
template_path = Path(__file__).parent / "../utils/templates"
env_path = Path(__file__).parent / "../utils/.env"
output_path = Path(__file__).parent / "../out"

logger.info(f"Template path: {template_path}")
logger.info(f"Env path: {env_path}")


# Load API key from .env file from path ./utils/.env
load_dotenv(dotenv_path=env_path)
logger.info(f"API key: {os.getenv('OPENAI_API_KEY')}")

# Load template from path ../utils/templates
templateLoader = jinja2.FileSystemLoader(searchpath=template_path)
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("resume-template.tex")

# Render template
outputText = template.render(
    test = "bruh"
)

# Write to file
with open(Path(output_path) / "test.tex", "w") as f:
    f.write(outputText)

