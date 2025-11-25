from notify.core import Notifier
from notify.channels import ConsoleEmailClientAdapter
from notify.schema import Message


def test_console_email_client_adapter(capsys):
    email_channel = ConsoleEmailClientAdapter(
        from_addr="from@test.com",
        to_addr="to@test.com"
    )
    notifier = Notifier(channel = email_channel)

    email_message = Message(
        subject="Test Subject",
        body="This is a test email body."
    )

    notifier.send(message=email_message)

    # capture the console output
    captured = capsys.readouterr().out

    assert "From: from@test.com" in captured
    assert "To: to@test.com" in captured

    assert "Subject: Test Subject" in captured

    assert "Body: This is a test email body." in captured