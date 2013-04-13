# EJS.tmLanguage

An EJS syntax definition specifically for sublime text.

This syntax definition uses <? and ?> for opening and closing tags, respectively. Here's an example:

	<div id='user-<?- userId ?>'>
		<?
		if (firstName && lastName)
		{
			?>
			Hello <?= firstName + lastName ?>
			<?
		}
		?>
	</div>

`<?` and `?>` where chosen because of the convenience to type on a qwerty keyboard. 
If you would like to change the open and closing tags in the syntax file to `<%` and `%>`, 
then change line 579 `<\?=?-?` to `<%=?-?` and 589 `\?>` to: `%>` in the EJS.tmLanguage file.

## Feedback

Feedback on this project is welcome. Let me know if you have problems with the syntax definition by creating a new GitHub issue.

Tips or donations are also very appreciated.

[![Gittip](https://www.gittip.com/assets/8.0.8/logo.png)](https://www.gittip.com/samholmes/)
[![PayPal Donation](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif "Donate using PayPal")](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=SJCCMHKZLMSX2&lc=US&item_name=EJS%2etmLanguage&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted)  
[<img src="https://en.bitcoin.it/w/images/en/c/c4/BC_Logotype_Reverse.png" height='18'>](bitcoin:1Ep5xmuRhFQREJ9BjPnySmtK3fxkWankDc) **1Ep5xmuRhFQREJ9BjPnySmtK3fxkWankDc**
