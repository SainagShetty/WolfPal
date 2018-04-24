class CoursesController < ApplicationController
  before_action :set_course, only: [:show, :edit, :update, :destroy]

  # GET /courses
  # GET /courses.json
  def index
    if params[:q].present?
      logger.debug "AFTER SUBMIT!!!!"

      clear_boolean(params[:q], :core_true)
      clear_boolean(params[:q], :schedules_project_true)
      clear_boolean(params[:q], :schedules_fieldwork_true)
      clear_select(params[:q], :schedules_semester_eq)

      logger.debug "KEYWORD IS -----"
      logger.debug params[:q][:course_name_cont]

      logger.debug "Calling PYTHON"
      pyscript_path = Rails.root.join('keyword-mapping/coursemap_to_user.py')
      tag_var = `python #{pyscript_path} #{params[:q][:course_name_cont]}`
      logger.debug tag_var
      logger.debug tag_var.is_a?(String)
      # make tag_var an array
      logger.debug "DONE!"

      tag_var.gsub!('[','')
      tag_var.gsub!(']','')
      tag_var.gsub!("'",'')

      all_codes=tag_var.split(',')

      logger.debug "ALL CODES ARRAY -"
      logger.debug all_codes

      logger.debug "Length of courseList"
      logger.debug all_codes.length
      logger.debug all_codes.is_a?(Array)

      @q = Course.includes(:schedules).ransack(params[:q])

      @courses = Course.includes(:schedules).joins(:schedules).where(code: all_codes)
      .order('courses.code')
      .page(params[:page])

    else
      @q = Course.includes(:schedules).ransack(params[:q])

      # @courses = Course.includes(:schedules).where(code: tag_var)
      # print(@q)

      @courses = @q.result(distinct: true)
                     .includes(:schedules)
                     .joins(:schedules)
                     .order('courses.code')
                     .page(params[:page])
    end

  end

  # GET /courses/1
  # GET /courses/1.json
  def show
  end

  # GET /courses/new
  def new
    @course = Course.new
  end

  # GET /courses/1/edit
  def edit
  end

  # POST /courses
  # POST /courses.json
  def create
    @course = Course.new(course_params)

    respond_to do |format|
      if @course.save
        format.html { redirect_to @course, notice: 'Course was successfully created.' }
        format.json { render :show, status: :created, location: @course }
      else
        format.html { render :new }
        format.json { render json: @course.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /courses/1
  # PATCH/PUT /courses/1.json
  def update
    respond_to do |format|
      if @course.update(course_params)
        format.html { redirect_to @course, notice: 'Course was successfully updated.' }
        format.json { render :show, status: :ok, location: @course }
      else
        format.html { render :edit }
        format.json { render json: @course.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /courses/1
  # DELETE /courses/1.json
  def destroy
    @course.destroy
    respond_to do |format|
      format.html { redirect_to courses_url, notice: 'Course was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_course
      @course = Course.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def course_params
      params.require(:course).permit(:code, :syllabus_file, :prerequisites, :course_name, :core, :channel_id)
    end

    def clear_boolean(q, condition)
      q.delete(condition) if q[condition] == "0"
    end

  def clear_select(q, condition)
    q.delete(condition) if q[condition] == "Any"
  end
end
