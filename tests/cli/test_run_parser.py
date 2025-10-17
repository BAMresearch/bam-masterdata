"""Tests for the run_parser function in bam_masterdata.cli.run_parser"""

import os
import tempfile
from unittest.mock import MagicMock

import pytest

from bam_masterdata.cli.run_parser import run_parser
from bam_masterdata.logger import log_storage
from bam_masterdata.metadata.entities import CollectionType, ObjectType
from bam_masterdata.metadata.definitions import ObjectTypeDef, PropertyTypeAssignment
from bam_masterdata.parsing import AbstractParser


class SampleObjectType(ObjectType):
    """Test object type for parser testing"""
    
    defs = ObjectTypeDef(
        code="TEST_OBJECT",
        description="Test object for parser testing//Test-Objekt für Parser-Tests",
        generated_code_prefix="TESTOBJ",
    )
    
    name = PropertyTypeAssignment(
        code="$NAME",
        data_type="VARCHAR",
        property_label="Name",
        description="Name of the test object//Name des Testobjekts",
        mandatory=True,
        show_in_edit_views=True,
        section="General information",
    )
    
    value = PropertyTypeAssignment(
        code="VALUE",
        data_type="INTEGER",
        property_label="Value",
        description="Value of the test object//Wert des Testobjekts",
        mandatory=False,
        show_in_edit_views=True,
        section="General information",
    )


class SimpleTestParser(AbstractParser):
    """Simple test parser that creates test objects"""
    
    def parse(self, files, collection, logger):
        """Parse files and add test objects to collection"""
        for file_path in files:
            # Read a simple test file
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    content = f.read().strip()
                    name = content or "Test Object"
            else:
                name = "Test Object"
            
            # Create a test object
            test_obj = SampleObjectType(name=name, value=42)
            obj_id = collection.add(test_obj)
            logger.info(f"Added test object with ID {obj_id}")


class ParserWithRelationships(AbstractParser):
    """Test parser that creates objects with relationships"""
    
    def parse(self, files, collection, logger):
        """Parse files and create parent-child relationships"""
        # Create parent object
        parent = SampleObjectType(name="Parent Object", value=100)
        parent_id = collection.add(parent)
        
        # Create child objects
        for i in range(2):
            child = SampleObjectType(name=f"Child Object {i}", value=i)
            child_id = collection.add(child)
            collection.add_relationship(parent_id, child_id)
        
        logger.info(f"Added parent and 2 child objects with relationships")


class ParserWithExistingCode(AbstractParser):
    """Test parser that references existing objects by code"""
    
    def parse(self, files, collection, logger):
        """Parse files and create object with existing code"""
        # Create an object with a specific code (to reference existing object)
        test_obj = SampleObjectType(name="Existing Object", value=999)
        test_obj.code = "EXISTING_OBJ_001"
        obj_id = collection.add(test_obj)
        logger.info(f"Added object with existing code: {test_obj.code}")


def test_run_parser_missing_openbis():
    """Test that run_parser returns early if openbis is None"""
    log_storage.clear()
    
    run_parser(
        openbis=None,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={},
    )
    
    # Check that an error was logged
    assert any("instance of Openbis must be provided" in log["event"] for log in log_storage)


def test_run_parser_missing_project_name(mock_openbis):
    """Test that run_parser returns early if project_name is empty"""
    log_storage.clear()
    
    run_parser(
        openbis=mock_openbis,
        space_name="TEST_SPACE",
        project_name="",  # Empty project name
        collection_name="TEST_COLLECTION",
        files_parser={},
    )
    
    # Check that an error was logged
    assert any("Project name must be specified" in log["event"] for log in log_storage)


def test_run_parser_empty_files_parser(mock_openbis):
    """Test that run_parser returns early if files_parser is empty"""
    log_storage.clear()
    
    run_parser(
        openbis=mock_openbis,
        space_name="TEST_SPACE",
        project_name="TEST_PROJECT",
        collection_name="TEST_COLLECTION",
        files_parser={},  # Empty files_parser
    )
    
    # Check that an error was logged
    assert any("No files or parsers to parse" in log["event"] for log in log_storage)


def test_run_parser_with_simple_parser(mock_openbis):
    """Test run_parser with a simple parser and test files"""
    log_storage.clear()
    
    # Create a temporary test file
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Data")
        test_file = f.name
    
    try:
        # Create parser instance and files dict
        parser = SimpleTestParser()
        files_parser = {parser: [test_file]}
        
        # Run the parser
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that objects were created in openbis
        assert len(mock_openbis._objects) > 0
        
        # Check logs for success messages
        # logs = log_storage  # log_storage is already a list
        assert any("Added test object" in log["event"] for log in log_storage)
        
    finally:
        # Clean up temp file
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_without_collection(mock_openbis):
    """Test run_parser without specifying a collection (objects attached to project)"""
    log_storage.clear()
    
    # Create a temporary test file
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Without Collection")
        test_file = f.name
    
    try:
        parser = SimpleTestParser()
        files_parser = {parser: [test_file]}
        
        # Run parser without collection name
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="TEST_PROJECT",
            collection_name="",  # No collection
            files_parser=files_parser,
        )
        
        # Check that warning was logged
        # logs = log_storage  # log_storage is already a list
        assert any("No Collection name specified" in log["event"] for log in log_storage)
        
        # Check that objects were still created
        assert len(mock_openbis._objects) > 0
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_creates_new_project(mock_openbis):
    """Test that run_parser creates a new project if it doesn't exist"""
    log_storage.clear()
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Data")
        test_file = f.name
    
    try:
        parser = SimpleTestParser()
        files_parser = {parser: [test_file]}
        
        # Get space and check initial project count
        space = mock_openbis.get_space("USER_TESTUSER")
        initial_project_count = len(space.get_projects())
        
        # Run parser with new project name
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="NEW_TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that new project was created
        final_project_count = len(space.get_projects())
        assert final_project_count == initial_project_count + 1
        
        # Check logs
        # logs = log_storage  # log_storage is already a list
        assert any("uppercase and underscores" in log["event"] for log in log_storage)
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_uses_existing_project(mock_openbis):
    """Test that run_parser uses an existing project if available"""
    log_storage.clear()
    
    # Create a project first
    space = mock_openbis.get_space("USER_TESTUSER")
    existing_project = space.new_project(code="EXISTING_PROJECT")
    existing_project.save()
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Data")
        test_file = f.name
    
    try:
        parser = SimpleTestParser()
        files_parser = {parser: [test_file]}
        
        initial_project_count = len(space.get_projects())
        
        # Run parser with existing project
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="EXISTING_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that no new project was created
        final_project_count = len(space.get_projects())
        assert final_project_count == initial_project_count
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_with_relationships(mock_openbis):
    """Test run_parser with a parser that creates parent-child relationships"""
    log_storage.clear()
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Relationships")
        test_file = f.name
    
    try:
        parser = ParserWithRelationships()
        files_parser = {parser: [test_file]}
        
        # Run parser
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that objects were created (parent + 2 children = 3)
        assert len(mock_openbis._objects) >= 3
        
        # Check logs for relationship creation
        # logs = log_storage  # log_storage is already a list
        assert any("Linked child" in log["event"] for log in log_storage)
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_with_existing_object_code(mock_openbis):
    """Test run_parser with a parser that references an existing object by code"""
    log_storage.clear()
    
    # Pre-create an object in openbis to simulate existing object
    space = mock_openbis.get_space("USER_TESTUSER")
    project = space.new_project(code="TEST_PROJECT")
    project.save()
    collection = mock_openbis.new_collection(
        code="TEST_COLLECTION", type="DEFAULT_EXPERIMENT", project=project
    )
    collection.save()
    
    # Create existing object
    identifier = "/USER_TESTUSER/TEST_PROJECT/TEST_COLLECTION/EXISTING_OBJ_001"
    existing_obj = mock_openbis.new_object(
        type="TEST_OBJECT",
        space=space,
        project=project,
        collection=collection,
        props={"name": "Old Name", "value": 1},
    )
    existing_obj.identifier = identifier
    mock_openbis._objects[identifier] = existing_obj
    space._objects[identifier] = existing_obj
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Existing Code")
        test_file = f.name
    
    try:
        parser = ParserWithExistingCode()
        files_parser = {parser: [test_file]}
        
        # Run parser
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check logs for update message
        # logs = log_storage  # log_storage is already a list
        assert any("already exists" in log["event"] and "updating properties" in log["event"] 
                   for log in log_storage)
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_multiple_parsers(mock_openbis):
    """Test run_parser with multiple parsers"""
    log_storage.clear()
    
    # Create multiple test files
    files = []
    for i in range(2):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=f"_{i}.txt") as f:
            f.write(f"Test Data {i}")
            files.append(f.name)
    
    try:
        # Create multiple parser instances with their files
        parser1 = SimpleTestParser()
        parser2 = ParserWithRelationships()
        files_parser = {
            parser1: [files[0]],
            parser2: [files[1]],
        }
        
        # Run parser
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that objects from both parsers were created
        # parser1: 1 object, parser2: 3 objects (1 parent + 2 children)
        assert len(mock_openbis._objects) >= 4
        
    finally:
        for f in files:
            if os.path.exists(f):
                os.unlink(f)


def test_run_parser_default_user_space(mock_openbis):
    """Test that run_parser uses default user space when specified space doesn't exist"""
    log_storage.clear()
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Data")
        test_file = f.name
    
    try:
        parser = SimpleTestParser()
        files_parser = {parser: [test_file]}
        
        # Run parser with non-existent space
        run_parser(
            openbis=mock_openbis,
            space_name="NON_EXISTENT_SPACE",
            project_name="TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that warning was logged about using user space
        # logs = log_storage  # log_storage is already a list
        assert any("does not exist" in log["event"] and "Loading space for" in log["event"] 
                   for log in log_storage)
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)


def test_run_parser_dataset_upload(mock_openbis):
    """Test that run_parser uploads files as datasets"""
    log_storage.clear()
    
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as f:
        f.write("Test Dataset")
        test_file = f.name
    
    try:
        parser = SimpleTestParser()
        files_parser = {parser: [test_file]}
        
        initial_dataset_count = len(mock_openbis._datasets)
        
        # Run parser
        run_parser(
            openbis=mock_openbis,
            space_name="USER_TESTUSER",
            project_name="TEST_PROJECT",
            collection_name="TEST_COLLECTION",
            files_parser=files_parser,
        )
        
        # Check that dataset was created
        final_dataset_count = len(mock_openbis._datasets)
        assert final_dataset_count > initial_dataset_count
        
        # Check logs for upload message
        # logs = log_storage  # log_storage is already a list
        assert any("Files uploaded to openBIS" in log["event"] for log in log_storage)
        
    finally:
        if os.path.exists(test_file):
            os.unlink(test_file)
