"""Published clinic content. See CONTENT_SOURCES.md for provenance and limits."""
BRANCHES = [
    dict(id='obrero', name='Obrero', city='Davao City', address='Door 2B STL Vntures Realty Bldg, Lacson St, Obrero, Davao City', phone='0917 803 6369', tel='+639178036369', email='gonzales.dental2020@gmail.com', facebook='https://www.facebook.com/gonzales.dentalclinic'),
    dict(id='matina', name='Matina', city='Davao City', address='Km 3 McArthur Highway, Davao City', phone='0927 339 6951', tel='+639273396951', email='gonzales.dental2024@gmail.com', facebook='https://www.facebook.com/profile.php?id=61559646209197'),
    dict(id='gensan', name='Gensan', city='General Santos City', address='Beatiles St, General Santos City', phone='0917 128 3972', tel='+639171283972', email='gdc.gensan2025@gmail.com', facebook='https://www.facebook.com/profile.php?id=61574243505145'),
    dict(id='digos', name='Digos', city='Digos City', address='1st Crumb Street, Digos', phone='0917 728 0698', tel='+639177280698', email='gdc.digos2025@gmail.com', facebook='https://www.facebook.com/profile.php?id=61579192551478'),
]
SERVICES = [
    dict(name='Consultation & diagnostics', category='general', note='Start with a consultation.', options=['Consultation and diagnostics']),
    dict(name='Cleaning & fluoride', category='general', note='Oral prophylaxis and fluoride treatment.', options=['Oral prophylaxis', 'Fluoride treatment']),
    dict(name='Orthodontics', category='alignment', note='Braces, retainers and Invisalign.', options=['Metal braces', 'Ceramic braces', 'Self-ligating braces', 'Retainers', 'Invisalign']),
    dict(name='Dental veneers', category='cosmetic', note='Composite, Emax and zirconia veneers.', options=['Composite veneers', 'Emax veneers', 'Zirconia veneers']),
    dict(name='Crowns & bridges', category='restorative', note='A range of crown and bridge materials.', options=['Plastic', 'Metal', 'Metal porcelain', 'Tilite', 'Emax', 'Ceramage', 'Zirconia']),
    dict(name='Tooth restorations', category='restorative', note='Fillings, inlays and onlays.', options=['Composite filling', 'Temporary filling', 'Inlays and onlays']),
    dict(name='Root canal treatment', category='restorative', note='Discuss root canal treatment with the clinic.', options=['Root canal treatment']),
    dict(name='Dentures & prostheses', category='restorative', note='Complete and partial denture options.', options=['Complete denture', 'Removable partial denture', 'Flexible denture', 'High impact / Ivocap denture']),
    dict(name='Oral surgery', category='general', note='Extractions and other surgical procedures.', options=['Tooth extraction', 'Third molar removal', 'Gingivectomy / gum surgery', 'Apicoectomy / root end surgery', 'Operculectomy']),
    dict(name='Cosmetic dentistry', category='cosmetic', note='Explore cosmetic care with your dentist.', options=['Cosmetic dentistry consultation']),
]

# Exact business identifiers resolved from the four user-supplied Google links.
MAP_RECORDS = {
    'obrero': ('2e63e27eb0e7ce93', 'JKBg5rr2LafxHpK3H', '4.6', 22),
    'matina': ('be69d0f7dc898c0f', 'wzJvZWlu6QbRTa3lv', '4.7', 7),
    'digos': ('ce5dff13382a0b2f', 'ZhR7nN7OZBvad3uE2', '5.0', 2),
    'gensan': ('7b6ad572a707845c', 'cGydQQ7SYYZsivHlo', '5.0', 1),
}
for branch in BRANCHES:
    cid, share, rating, count = MAP_RECORDS[branch['id']]
    branch.update(
        cid=str(int(cid, 16)),
        map_url='https://www.google.com/maps?cid=' + str(int(cid, 16)),
        map_embed='https://www.google.com/maps?cid=' + str(int(cid, 16)) + '&output=embed',
        source_map='https://share.google/' + share,
        rating=rating, review_count=count,
        url='/clinics/' + branch['id'] + '/',
    )
BRANCHES[1]['address'] = 'Door 5, MS Land Complex, Km 3 McArthur Highway, Talomo, Davao City'

# Concise paraphrases of the corresponding published WordPress service pages.
SERVICE_DETAILS = [
    ('consultation', 'consultation-and-diagnostics',
     'A consultation brings together your concerns, medical history and an examination of your teeth. It is the starting point for an individual treatment plan.',
     [('Your first conversation', 'Tell the dentist about your symptoms, medical conditions, medicines and allergies. This information helps the team understand your needs.'), ('Diagnostics when needed', 'Your dentist may recommend X-rays or other tests depending on the findings. Not every consultation requires the same tests.'), ('Photographs and privacy', 'The clinic’s published guidance describes asking permission for clinical photographs and protecting patient information.')]),
    ('cleaning-fluoride', 'oral-prophylaxis-and-fluoride',
     'Professional cleaning removes hardened deposits from teeth. Fluoride treatment supports tooth enamel and helps prevent cavities.',
     [('Oral prophylaxis', 'The clinic describes removing tartar that cannot be removed through ordinary brushing alone.'), ('Fluoride treatment', 'Your dentist can advise whether professional fluoride treatment is appropriate and how often you need it.')]),
    ('orthodontics', 'orthodontics',
     'Orthodontic care addresses the position of teeth. Assessment comes first: the appliance and treatment plan depend on your individual case.',
     [('Braces', 'The published options include conventional metal braces, tooth-coloured ceramic braces and self-ligating braces.'), ('Aligners and retainers', 'Invisalign and retainers are also listed. Ask the clinic about suitability, follow-up appointments and the commitment involved.')]),
    ('veneers', 'dental-veneers',
     'Veneers are thin coverings placed over the front surfaces of teeth to change their appearance, including shape, shade and size.',
     [('Choosing a material', 'The clinic lists composite, Emax and zirconia veneers. Your dentist can explain differences in preparation, maintenance and suitability.'), ('Planning your visits', 'Some veneer options involve several visits to check the fit and shade before placement. Treatment and longevity vary by case; no result is guaranteed.')]),
    ('crowns-bridges', 'dental-crowns-and-bridges',
     'A crown covers an existing tooth. A bridge replaces one or more missing teeth with a fixed restoration.',
     [('Materials and planning', 'The clinic publishes several material options. Selection depends on the tooth, the restoration and the dentist’s assessment.'), ('Before you decide', 'Ask about tooth preparation, the proposed material, the number of visits, maintenance and the full treatment estimate.')]),
    ('restorations', 'tooth-restorations',
     'Restorative treatment repairs tooth structure affected by decay or damage. A dental assessment determines whether a filling or another approach is appropriate.',
     [('Fillings', 'Composite fillings use tooth-coloured material. Temporary fillings are also listed in the clinic’s service directory.'), ('Inlays and onlays', 'These restorations are made outside the mouth and fitted to the tooth. They may be considered when a cavity is too large for a simple filling.')]),
    ('root-canal', 'root-canal-treatment',
     'Root canal treatment removes infected tissue inside a tooth, cleans and seals the canals, and restores the tooth rather than extracting it.',
     [('Assessment first', 'Examination and diagnostic tests help the dentist decide whether root canal treatment is appropriate for your tooth.'), ('A course of care', 'The number of visits depends on the case. A final restoration, sometimes a crown, may be needed. Ask your dentist about risks, alternatives and follow-up.')]),
    ('dentures', 'dentures-and-prostheses',
     'Dentures replace missing teeth. Partial dentures are used when some natural teeth remain; complete dentures replace a full set of missing teeth.',
     [('Finding the right fit', 'The clinic lists plastic, flexible, metal-framework, high-impact and Ivocap options. Your dentist can explain which designs suit your mouth.'), ('Getting used to dentures', 'New dentures can take time to get used to. Ask the clinic about fit checks, cleaning and follow-up if you experience rubbing or soreness.')]),
    ('oral-surgery', 'oral-surgery',
     'The clinic’s surgical services include tooth extractions, wisdom-tooth removal and selected procedures involving the gums and tooth roots.',
     [('A case-by-case decision', 'Not every wisdom tooth needs removal. Examination and imaging, when indicated, help determine the appropriate treatment.'), ('Medical history matters', 'Tell the dentist about your medicines, allergies and medical conditions. Some cases need medical clearance or referral to an oral surgeon.')]),
    ('cosmetic-dentistry', 'cosmetic-procedures',
     'Cosmetic dentistry focuses on the appearance of teeth and gums. The clinic publishes options for tooth colour, shape, gaps and gum appearance.',
     [('Published options', 'These include whitening, gum contouring, gum depigmentation, gap closure and tooth reshaping. Internal bleaching is discussed for root-canal-treated teeth.'), ('Plan before treatment', 'An assessment helps identify a suitable approach. Discuss preparation, limitations, maintenance and costs before deciding.')]),
]
for service, (slug, source_slug, description, sections) in zip(SERVICES, SERVICE_DETAILS):
    service.update(slug=slug, description=description, sections=sections,
                   source='https://gonzalesdentalclinic.wordpress.com/services/' + source_slug + '/')
SERVICES[-1]['options'] = ['Gum contouring', 'Gum depigmentation', 'Diastema / gap closure', 'Tooth whitening', 'Enameloplasty / tooth reshaping', 'Internal tooth bleaching']
SERVICES[-1]['note'] = 'Tooth whitening, shaping and gum aesthetics.'
SERVICES[8]['options'].append('Frenectomy / frenuloplasty')
SERVICES[7]['options'].append('Metal-framework partial dentures')

FAQS = [
    dict(question='How do I arrange an appointment?', answer='Choose your branch and use its phone number or Facebook page to contact the team. The clinic will confirm your appointment directly; this website does not reserve a time slot.'),
    dict(question='How early should I arrive?', answer='The clinic’s published first-visit guide recommends arriving 5–10 minutes before your appointment to allow time for patient records. Confirm any branch-specific instructions when booking.'),
    dict(question='What happens at my first visit?', answer='The published guide describes completing patient forms, being guided to the treatment area, and receiving instructions after treatment. A consultation considers your dental concerns and medical history.'),
    dict(question='What should I tell the dentist?', answer='Share your concerns, medical conditions, medicines and allergies. Ask your branch what records to bring and which current arrival or infection-control requirements apply.'),
    dict(question='Will I need a dental X-ray?', answer='Not every case requires an X-ray. The clinic’s consultation guide explains that additional tests depend on the examination and the condition being assessed.'),
    dict(question='What payment methods do you accept?', answer='Please ask your chosen branch before your visit. The older website’s payment page does not publish a list of accepted methods, so card, e-wallet, instalment and insurance arrangements need confirmation.'),
    dict(question='Are all services available at every branch?', answer='The service directory represents the group’s published treatments. Contact your branch to confirm availability, the appropriate dentist and an estimate for your case.'),
    dict(question='Where can I check opening hours?', answer='Use the branch’s Google listing or contact its team. Confirm the schedule before travelling, especially for holidays or an evening appointment.'),
]

HISTORY = [
    ('1960', 'A family practice begins', 'Dr. Cornelia “Nelly” Gonzales established a private practice after working as a government dentist. The early clinic had locations in Mintal and on San Pedro Street.'),
    ('1975', 'The second generation', 'Dr. Nelly consolidated the practice at Aldevinco in central Davao and opened a dental supply store. Her newly licensed son, Dr. Dean Gonzales, began working alongside her.'),
    ('1999', 'A home in Obrero', 'The practice moved to the corner of Porras and Lacson Streets in Obrero. Dr. Dean later took over following Dr. Nelly’s retirement.'),
    ('Third generation', 'The story continues', 'Dr. Alyssa Gonzales joined her father in practice, continuing the family’s work in dentistry. The group now has clinics in Obrero, Matina, General Santos and Digos.'),
]
