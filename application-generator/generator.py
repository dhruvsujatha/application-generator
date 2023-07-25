#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from pathlib import Path
import argparse

import jinja2
from dotenv import load_dotenv

# Setup ArgParse
parser = argparse.ArgumentParser(description="Generate a resume from a template.")
parser.add_argument(
    "-t",
    "--type",
    type=str,
    choices=["cs", "ds", "hpc"],
    default="cs",
    help="Type of resume to generate.",
) 
parser.add_argument(
    "-e",
    "--excerpt",
    type=str,
    required=True,
    help="Excerpt which includes the keywords from the job description.",
)
args = parser.parse_args()

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

