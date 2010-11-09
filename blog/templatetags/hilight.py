from django import template 
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import guess_lexer
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from BeautifulSoup import BeautifulSoup
from django.contrib.markup.templatetags.markup import textile

register = template.Library()

@stringfilter #expects string 
def syntax_hilight(content):
	try:

		soup = BeautifulSoup(content) #initial content soup

		codeblocks = soup.findAll('code')
		for block in codeblocks: #remove code and replace with "removed"
			block.replaceWith('<code class="removed"></code>')

		textiled = textile(str(soup)) #convert content via textile
		soup = BeautifulSoup(textiled) #new soup on converted

		empty_code_blocks, index = soup.findAll('code', 'removed'), 0 #grab "removed #grab "removed""

		for block in codeblocks:
			lexer = guess_lexer(block.renderContents())
			empty_code_blocks[index].replaceWith(highlight(block.renderContents(), lexer, HtmlFormatter()))
			index += 1
		content = soup
	except Exception, e:
		pass
	return mark_safe(content) 
register.filter('hilite', syntax_hilight)
