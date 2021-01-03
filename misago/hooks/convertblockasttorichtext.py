from typing import Optional

from ..types import (
    ConvertBlockAstToRichTextAction,
    ConvertBlockAstToRichTextFilter,
    GraphQLContext,
    ParsedMarkupMetadata,
    RichTextBlock,
)
from .filter import FilterHook


class ConvertBlockAstToRichTextHook(
    FilterHook[ConvertBlockAstToRichTextAction, ConvertBlockAstToRichTextFilter]
):
    is_async = False

    def call_action(
        self,
        action: ConvertBlockAstToRichTextAction,
        context: GraphQLContext,
        ast: dict,
        metadata: ParsedMarkupMetadata,
    ) -> Optional[RichTextBlock]:
        return self.filter(action, context, ast, metadata)
