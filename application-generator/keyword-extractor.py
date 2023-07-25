#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keybert import KeyBERT
import logging
import argparse

# Setup ArgParse
parser = argparse.ArgumentParser(description="Extract keywords from a job description.")
parser.add_argument(
    "-d",
    "--description",
    type=str,
    required=True,
    help="Job description to extract keywords from.",
)
args = parser.parse_args()

# Set up logging
logger = logging.getLogger(__name__)

# Extract keywords

doc = """
Systems Engineers at Walmart should have a passion for and experience with either Windows OS, Mac OS, or Linux.  

Participates in agile teams supporting systems engineering projects by collaborates with the project team to build systems engineering solutions; translates requirements into potential solutions based on existing options; develops solutions to meet business needs; collaborates with the project team to build systems engineering solutions; and ensures solutions align with the overall project design. 

Troubleshoots issues related to systems engineering solutions by serving as software operational support; researches and reviews reported issues; evaluates the impact to the business and executes tasks as designated in the action plan; performs root cause analysis to reduce future issues; and engages support teams when needed. 

Supports the daily operations for existing systems engineering solutions by performs maintenance and monitors the health and performance of systems engineering solutions; participates in the development and delivery of operational features and operations management systems and processes to accommodate growth and traffic on eCommerce websites; participates in systems testing; reviews logs in order to identify and document 
issues; executes daily requirements in order to ensure reliable and continued service; documents systems engineering processes and designs. 

Demonstrates up-to-date expertise and applies this to the development, execution, and improvement of action plans by providing expert advice and guidance to others in the application of information and best practices; supporting and aligning efforts to meet customer and business needs; and building commitment for perspectives and rationales. 

Provides and supports the implementation of business solutions by building relationships and partnerships with key stakeholders; identifying business needs; determining and carrying out necessary processes and practices; monitoring progress and results; recognizing and capitalizing on improvement opportunities; and adapting to competing demands, organizational changes, and new responsibilities. 

Models compliance with company policies and procedures and supports company mission, values, and standards of ethics and integrity by incorporating these into the development and implementation of business plans; using the Open Door Policy; and demonstrating and assisting others with how to apply these in executing business processes and practices. 
"""

kw_model = KeyBERT()

doc_embeddings, word_embeddings = kw_model.extract_embeddings(args.description)

keywords = kw_model.extract_keywords(args.description, doc_embeddings=doc_embeddings, word_embeddings=word_embeddings)

print(keywords)