;(function($) {
	// Are we on the right page?
	if(location.href.match(/comments\/r\//)) {

		$(document).on('keydown', function(e) {
			e.preventDefault();
				
			// Up key, get previous root comment
			if(e.which == 38) {
				var next = find_comment('prev');

			// Down key, get next root comment
			} else if(e.which == 40) {
				var next = find_comment('next');
			}

			// Get top offset of found comment
			var offset = next.offset().top;

			// Scroll to it
			$('html, body').stop().animate({
				scrollTop: offset - 17
			}, 200);
		});
	}


	// Finds previous or next comment relative to current scroll position
	function find_comment(find) {
		var selector = '.two > .indent',
			all = $(selector),
			scroll = $(document).scrollTop(),
			found;

		// Loop through all root comments
		all.each(function() {
			var elem = $(this),
				offset = elem.offset().top;

			// If we're going UP, and offset is less than current scroll
			if(find == 'prev' && offset < scroll) {
				found = elem;
				return true;

			// If we're going DOWN, and offset is more than current scroll
			} else if(find == 'next' && offset > scroll+30) {
				found = elem;
				return false;
			}
		});

		return found || all.first();
	}
})(jQuery);