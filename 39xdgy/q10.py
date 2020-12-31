'''
!!!!!
Regular Expression Matching

'''
def isMatch(self, s: str, p: str) -> bool:

	@lru_cache(None)
	def is_match_after(i=0, j=0):
		'''does the string s[i:] match pattern[j:]'''
		if i >= len(s) and j >= len(p): return True  # processed both
		if j >= len(p): return False
		sch = s[i:i+1]
		pch = p[j:j+1]
		is_asterix = p[j+1:j+2] == '*'
		is_dot = pch == '.'

		# try skip the char if followed by asterix
		# if above doesn't work this has to be a match or a dot
		# and the rest has to match
		return is_asterix and is_match_after(i, j+2) or \
			   (sch == pch or is_dot and sch) and \
			   (is_match_after(i+1, j+1+is_asterix) or is_asterix and is_match_after(i+1, j)) 

	return is_match_after()