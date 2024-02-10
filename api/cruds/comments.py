from sqlalchemy.ext.asyncio import AsyncSession

from api.models import models
import api.schemas.comment as comment_schema


async def post_comment(
    db: AsyncSession, plan_id: int, comment: comment_schema.CommentCreate
):
    """Create a comment for a plan."""
    db_comment = models.Comment(
        plan_id=plan_id, comment=comment.comment, stars=comment.stars
    )
    db.add(db_comment)

    await db.commit()
    await db.refresh(db_comment)

    return db_comment
