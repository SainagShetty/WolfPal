json.extract! course, :id, :code, :syllabus_id, :prerequisites, :course_name, :core, :channel_id, :created_at, :updated_at
json.url course_url(course, format: :json)
