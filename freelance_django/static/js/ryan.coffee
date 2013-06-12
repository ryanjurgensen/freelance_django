$(document).ready () ->
	$.tablesorter.addParser { 
		id: 'skillz', 
		is: (s) -> 
			return false
		, 
		format: (s) -> 
			return s.toLowerCase().replace(/high/,2).replace(/medium/,1).replace(/low/,0); 
		, 
		type: 'numeric' 
	}

	$("#skills-table").tablesorter {
		sortList: [[1,1], [2,1]],
		headers: { 
			1: { 
				sorter:'skillz' 
			} 
			2: { 
				sorter:'skillz' 
			}
		}
	}

	$('#gist-hover').click (e) ->
		$('.gist').toggle()

	$('.foursquare').click (e) ->
		#duration for all animations
		time = 350
		if $(this).hasClass 'big'
			#collapse this one and expand all others
			$('.foursquare').show().animate {width: window.startingWidth, height: window.startingWidth}, time
			$(this).removeClass 'big'
		else
			window.startingWidth = $(this).width()
			#the starting size is variable in LESS, so calculate the expanded size.
			expanded = ($(this).width() * 2) + (2 * parseInt($(this).css 'margin-top'))
			#collapse the box right next to the clicked one
			$(this).siblings().animate {width: "0px"}, time
			#find the other row, then collapse all the boxes.
			$(this).parent().siblings().find('div').each (e) ->
				$(this).animate {height: "0px"}, time
			#finally, expand the clicked one and hide the rest when done
			$(this).animate {width: expanded, height: expanded}, time, (e) ->
				$('.foursquare').not($(this)).hide()
				$(this).addClass 'big'
				return
		return

	$('#show-table').click (e) ->
		$('#skills-row').toggle()
		return

	$('.tile img, .tile .blk-label, .tile .blk-label label').click (e) ->
		$('.modal-body').html $(this).siblings('.desc').html()
		tagName = $(e.target).prop("tagName")
		title = ''
		if tagName == 'LABEL'
			title = $(this).html()
		else if tagName == 'DIV'
			title = $(this).find('label').html()
		else
			title = $(this).siblings('.blk-label').find('label').html()
		$('#modalLabel').html title
		$('#portfolioModal').modal('show')
		_gaq.push(['_trackEvent', 'Portfolio', title]);
		return

	$('#freeOfficeButton').click (e) ->
		_gaq.push(['_trackEvent', 'Buttons', 'Office Hours']);
		return

	$('#hireBtn').click (e) ->
		_gaq.push(['_trackEvent', 'Buttons', 'Hire']);
		return

	return

	$('.veteranButton').click (e) ->
		btn =  $($(this).siblings('.veteranImageInput')[0])
		e.preventDefault();

		if meta_image_frame
			meta_image_frame.open();	
			return

		meta_image_frame = wp.media.frames.meta_image_frame = wp.media({
		title: meta_image.title,
		button: { text:  meta_image.button },
		library: { type: 'image' }
		})

		meta_image_frame.on 'select', do (btn, meta_image_frame) ->
			media_attachment = meta_image_frame.state().get('selection').first().toJSON()
			btn.val(media_attachment.url)
			return

		meta_image_frame.open()
		return
