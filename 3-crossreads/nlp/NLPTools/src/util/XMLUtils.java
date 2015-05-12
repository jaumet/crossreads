package util;

import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;

import org.w3c.dom.Document;
import org.w3c.dom.NamedNodeMap;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class XMLUtils {

	/**
	 * Creates a string buffer of spaces
	 * @param depth the number of spaces
	 * @return string of spaces
	 */
	private static StringBuffer Pad(int depth) {
		StringBuffer sb = new StringBuffer();
		for (int i = 0; i < depth; i++)
			sb.append("  ");
		return sb;
	}

	public static void PrintNode(Node n) {
		PrintNode(n, "", 0);
	}
	
	/**
     * Print the DOM tree on stdout
     * @param n root node of a document
     * @param prefix
     * @param depth
     */
	private static void PrintNode(Node n, String prefix, int depth) {

		try {
			System.out.print("\n" + Pad(depth) + "[" + n.getNodeName());
			NamedNodeMap m = n.getAttributes();
			for (int i = 0; m != null && i < m.getLength(); i++) {
				Node item = m.item(i);
				System.out.print(" " + item.getNodeName() + "="
						+ item.getNodeValue());
			}
			System.out.print("] ");

			boolean has_text = false;
			if (n.getNodeType() == Node.TEXT_NODE) {
				has_text = true;
				String valn = n.getNodeValue().trim();
				if (valn.length() > 0)
					System.out.print("\n" + Pad(depth) + " \"" + valn + "\"");
			}

			NodeList cn = n.getChildNodes();

			for (int i = 0; cn != null && i < cn.getLength(); i++) {
				Node item = cn.item(i);
				if (item.getNodeType() == Node.TEXT_NODE) {
					String val = item.getNodeValue().trim();
					if (val.length() > 0)
						System.out.print("\n" + Pad(depth) + val + "\"");
				} else
					PrintNode(item, prefix, depth + 2);
			}
		} catch (Exception e) {
			System.out.println(Pad(depth) + "Exception e: ");
		}
	}

	public static Object XPathQuery(XPath xpath, Document doc, String query, boolean string_only) {
		
		try {
			XPathExpression xPathExpression = xpath.compile(query);
			if (string_only)
				return xPathExpression.evaluate(doc);
			else
				return xPathExpression.evaluate(doc, XPathConstants.NODESET);
		} catch (XPathExpressionException e) {
			e.printStackTrace();
			return null;
		}
	}

}
