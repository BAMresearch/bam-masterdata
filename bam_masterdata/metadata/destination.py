from pydantic import BaseModel, Field, model_validator


class Destination(BaseModel):
    """
    Destination override for storing an object in openBIS.

    Any field left unset is inherited from the default destination configured in RunParsers.
    """

    space: str | None = Field(
        default=None,
        description="openBIS space code to use for this object. If omitted, the space selected in RunParsers is used.",
    )

    project: str | None = Field(
        default=None,
        description="openBIS project code to use for this object. If omitted, the project selected in RunParsers is used.",
    )

    collection: str | None = Field(
        default=None,
        description="openBIS collection code to use for this object. If omitted, the object is stored directly in the resolved project.",
    )

    @model_validator(mode="after")
    def validate_collection_requires_project(self):
        if self.collection is not None and self.project is None:
            raise ValueError(
                "`project` must be specified when `collection` is specified."
            )

        return self
