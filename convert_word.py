import zipfile
import xml.etree.ElementTree as ET

doc = zipfile.ZipFile('joskiy_instruction.docx').read('word/document.xml')
root = ET.fromstring(doc)
# Microsoft's XML makes heavy use of XML namespaces; thus, we'll need to reference that in our code
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
body = root.find('w:body', ns)  # find the XML "body" tag
p_sections = body.findall('w:p', ns)  # under the body tag, find all the paragraph sections

for p in p_sections:
    text_elems = p.findall('.//w:t', ns)
    print(''.join([t.text for t in text_elems]))
    # print()
    
def is_heading2_section(p):
    """Returns True if the given paragraph section has been styled as a Heading2"""
    return_val = False
    heading_style_elem = p.find(".//w:pStyle[@w:val='Heading3']", ns)
    if heading_style_elem is not None:
        return_val = True
    return return_val


def get_section_text(p):
    """Returns the joined text of the text elements under the given paragraph tag"""
    return_val = ''
    text_elems = p.findall('.//w:t', ns)
    if text_elems is not None:
        return_val = ''.join([t.text for t in text_elems])
    return return_val
 
 
section_labels = [get_section_text(s) if is_heading2_section(s) else '' for s in p_sections]
print(section_labels)
# section_text = [{'title': t, 'text': get_section_text(p_sections[i+1])} for i, t in enumerate(section_labels) if len(t) > 0]
