import yagmail
import os

path = 'FaceRecognitionRpi/Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
date_ed = newest[11:-4]

sub = f"Attendance Report for {date_ed}"
body = f"Attendance for {date_ed} Can be Downloaded"

# Gmail Info
yag = yagmail.SMTP("ljay88944@gmail.com", "DELTADRAGON")
receiver = "jaydambal50@gmail.com"
# Mail sending
print(f"Sending Mail for date -> {date_ed}, as this is the new File Available")
yag.send(
    to=receiver,
    subject=sub,
    contents=body,
    attachments=filename
)
print("Email Sent Succesfully!")
