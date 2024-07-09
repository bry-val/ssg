# ol_block = """1. An elaborate pantheon of deities (the `Valar` and `Maiar`)
# 2. The tragic saga of the Noldor Elves
# 3. The rise and fall of great kingdoms such as Gondolin and Númenor"""
#
# print(check_ordered_list(ol_block))
#
# md = """ This is **bolded** paragraph
#
# >This is another paragraph with *italic* text and `code` here
# >This is the same paragraph on a new line
#
# * This is a list **there is also bold** and *italics*
# * with items and inline `code` tags.
#
# 1. This is another **paragraph** with *italic* text and `code` here
# 2. This is the same paragraph on a new line
#
# This is another paragraph with *italic* text and `code` here
# This is the *same* `paragraph` on a new line
#
# ```
# for i in range(3):
#     print(i)
# ```
#
# ### This is the same *paragraph* `on` **a new line**
#
# """

# ul_block = markdown_to_blocks(md)[2]
# quote_block = markdown_to_blocks(md)[1]
# ol_block = markdown_to_blocks(md)[3]
# p_block = markdown_to_blocks(md)[4]
# code_block = markdown_to_blocks(md)[5]
# heading_block = markdown_to_blocks(md)[6]


# print(block_to_html(ul_block, BLOCK_TYPE_UNORDERED_LIST))
# print(block_to_html(quote_block, BLOCK_TYPE_QUOTE))
# print(block_to_html(ol_block, BLOCK_TYPE_ORDERED_LIST))
# print(block_to_html(p_block, BLOCK_TYPE_PARAGRAPH))
# print(block_to_html(code_block, BLOCK_TYPE_CODE))
# print(block_to_html(heading_block))


# quote_block = """> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to
# > detect its presence.
# > I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
# > I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the
# > other in the purposed domination of the author."""
#
# print(quote_to_html(quote_block))

# md_block = """- **Diverse Cultures and Languages**: Each race, from the noble Elves to the sturdy Dwarves, is endowed with its own
#   rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as
#   Quenya and Sindarin, each with its own grammar and lexicon.
# - **Geographical Realism**: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of
#   Mordor, is depicted with such vividness that it feels as tangible as our own world.
# - **Historical Depth**: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at
#   bygone eras, giving the world a lived-in, authentic feel."""
#
# md_ul_block = """- The resilience of the human (and hobbit) spirit in the face of overwhelming odds
# - The corrupting influence of power, epitomized by the One Ring
# - The importance of friendship, loyalty, and sacrifice"""
#
# not_ul = """These universal themes lend the series a profound philosophical depth, making it a beacon of wisdom and insight for
# generations of readers."""
#
# print("nested bold in UL:", ul_to_html(md_block))
# print("known ulblock:", ul_to_html(md_ul_block))
# print("not ulblock:", block_to_block_type(not_ul))
